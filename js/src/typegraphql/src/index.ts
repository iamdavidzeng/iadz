import 'reflect-metadata';
import * as Express from 'express';
import { ApolloServer } from "apollo-server-express";
import { buildSchema, Query, Resolver } from "type-graphql";


@Resolver()
class HelloResolver {
    @Query(() => String)
    async hello() {
        return "Hello, world!";
    }
}

async function main() {
    const schema = await buildSchema({
        resolvers: [HelloResolver],
    });

    const app = Express()

    const server = new ApolloServer({
        schema,
    })

    server.applyMiddleware({ app })

    app.listen(4000, () =>
        console.log("Server is running on http://localhost:4000/graphql 🚀🚀🚀")
    )
}

main()