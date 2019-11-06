"use strict";

const amqp = require("amqplib");
const uuid = require("uuid/v4");

const replyToId = uuid();
const rpcResolvers = {};
let connection;
let channel;

function consumeQueue(message) {

    const correlationId = message.properties.correlationId;

    if (correlationId in rpcResolvers) {
        const rawContent = JSON.parse(message.content.toString());
        
        const resolver = rpcResolvers[correlationId];
        rpcResolvers[correlationId] = undefined;
        
        if (rawContent.error) {

            console.log("erros: " + rawContent.error);
            resolver.reject(
                new Error("Error: " + rawContent.error)
            );
        } else {
            resolver.resolve(rawContent.result);
        }
    }
};

async function connect() {
    connection = await amqp.connect("amqp://localhost");
    channel = await connection.createChannel();

    const queueName = `reply-to-cc-gatway-${replyToId}`;

    const queueInfo = await channel.assertQueue(queueName, {
        exclusive: true,
        autoDelete: true,
        durable: false,
    });

    await channel.bindQueue(queueInfo.queue, "nameko-rpc", replyToId);
    
    await channel.consume(queueInfo.queue, consumeQueue, {
        noAck: true,
    });
}

async function callRpc(
    serviceName,
    functionName,
    rpcPayload
) {
    const routingKey = `${serviceName}.${functionName}`;
    const correlationId = uuid();

    return new Promise((resolve, reject) => {
        if (!channel) {
            console.log("Fail to create channel!!!");
        }

        rpcResolvers[correlationId] = { resolve, reject };

        const payload = {
            args: rpcPayload.args ? rpcPayload.args : [],
            kwargs: rpcPayload.kwargs ? rpcPayload.kwargs : {},
        }

        console.log(payload);

        channel.publish(
            "nameko-rpc",
            routingKey,
            Buffer.from(JSON.stringify(payload)),
            {
                correlationId,
                replyTo: replyToId,
                contentEncoding: 'utf-8',
                contentType: 'application/json',
                deliveryMode: 2,
                priority: 0,
            }
        );
    })
}

function rpcProxy() {
    return new Proxy(
        {},
        {
            get(target, serviceName) {
                return new Proxy(
                    { serviceName },
                    {
                        get(target, methodName) {
                            return payload => callRpc(
                                target.serviceName,
                                methodName,
                                payload,
                            )
                        }
                    }
                )
            }
        }
    )
}


function rpcMiddleware(req, _, next) {
    req.rpc = rpcProxy();

    next();
}

module.exports = {
    rpcMiddleware: rpcMiddleware,
}
