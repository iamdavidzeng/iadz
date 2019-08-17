const express = require("express");
const { ApolloServer } = require("apollo-server-express");
const { schema } = require("./schemas");
const { resolvers } = require("./resolvers");

const app = express();

const server = new ApolloServer({
    typeDefs: schema,
    resolvers,
});

server.applyMiddleware({ app, path: "/graphql" });

app.listen({ port: 8000 }, () => {
    console.log("Apollo Server runnning on http://localhost:8000/graphql");
});
