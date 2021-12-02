import 'reflect-metadata';
import * as Express from 'express';
import { ApolloServer } from 'apollo-server-express';
import { buildSchema } from 'type-graphql';
import { authChecker } from './auth-checker';
import { ExampleResolver } from './resolvers';
import { Context } from 'apollo-server-core';
import { useSofa } from 'sofa-api';

async function main() {
  const schema = await buildSchema({
    resolvers: [ExampleResolver],
    authChecker,
  });

  const app = Express();
  app.use('/api', useSofa({ basePath: '/api', schema }));

  const server = new ApolloServer({
    schema,
    context: () => {
      const ctx: Context = {
        user: {
          id: 1,
          name: 'Sample user',
          roles: ['REGULAR'],
        },
      };
      return ctx;
    },
  });

  server.applyMiddleware({ app });

  app.listen(4000, '0.0.0.0', () =>
    console.log('Server is running on http://localhost:4000/graphql 🚀🚀🚀')
  );
}

main();
