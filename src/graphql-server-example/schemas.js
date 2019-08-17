const { gql } = require("apollo-server-express");

const schema = gql`
    type User {
        username: String!
    }

    type Query {
        me: User
    }
`;

module.exports = {
    schema: schema,
};
