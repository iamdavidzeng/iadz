import 'reflect-metadata';
import * as Express from 'express';
import { ApolloServer } from "apollo-server-express";
import { buildSchema, Query, Resolver } from "type-graphql";
import { authChecker } from './auth-checker';


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
        authChecker,
    });

    const app = Express()

    const server = new ApolloServer({
        schema,
        context: () => {
            const ctx = {
                user: {
                    id: 1,
                    name: "Sample user",
                    roles: ["REGULAR"],
                }
            }
            return ctx;
        }
    })

    server.applyMiddleware({ app })

    app.listen(4000, () =>
        console.log("Server is running on http://localhost:4000/graphql 🚀🚀🚀")
    )
}

main()