const express = require("express");
const { ApolloServer } = require("apollo-server-express");
const { schema } = require("./schemas");
const { resolvers } = require("./resolvers");
const { rpcMiddleware } = require("./rpc_server");

const app = express();

const server = new ApolloServer({
    typeDefs: schema,
    resolvers,
    context: ({ req, res }) => ({
        req,
        res,
        rpc: req.rpc,
    })
});

app.use(rpcMiddleware);

server.applyMiddleware({ app, path: "/graphql" });

app.listen({ port: 8080 }, () => {
    console.log("Apollo Server runnning on http://localhost:8080/graphql");
});
