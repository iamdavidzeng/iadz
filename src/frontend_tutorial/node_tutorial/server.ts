import * as express from "express";
import { ApolloServer } from "apollo-server-express";
import { namekoRpcContextMiddleware } from "./middleware/rpc";
import { createServer } from "http";
import * as cors from "cors";
import schema from "./schema";
import compression from "compression";
import depthLimit from "graphql-depth-limit";


const app = express();

const server = new ApolloServer({
    schema,
    validationRules:[depthLimit(7)],
    context: ({ req, res }) => ({
        req,
        res,
        rpc: req.rpc,
    })
});

app.use("*", cors());
app.use(compression());
app.use(namekoRpcContextMiddleware);

server.applyMiddleware({ app, path: "/graphql" });

const httpServer = createServer(app);

httpServer.listen(
    { port: 8080 },
    (): void => console.log(`running on http://localhost:8080/graphql`)
);