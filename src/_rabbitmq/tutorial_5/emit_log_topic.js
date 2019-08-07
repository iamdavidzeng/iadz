#! /usr/bin/env node

var amqp = require("amqplib/callback_api");

amqp.connect("amqp://localhost", function(error0, conneciton) {
    if (error0) {
        throw error0;
    }

    conneciton.createChannel(function(error1, channel) {
        if (error1) {
            throw error1;
        }

        var exchange = "topic_logs";
        var args = process.argv.slice(2);
        var key = (args.length > 0) ? args[0] : "anonymous.info";
        var msg = args.slice(1).join(" ") || "Hello, World!";

        channel.assertExchange(exchange, "topic", {
            durabl: false
        });
        channel.publish(exchange, key, Buffer.from(msg));
        console.log("[x] Sent %s:%s", key, msg);
    });

    setTimeout(function() {
        conneciton.close();
        process.exit(0)
    }, 500);
});
