const { gql } = require("apollo-server-express");

const schema = gql`
    type User {
        email_verified: Boolean
        phone: String
        email: String
        enabled: Boolean
    }

    type Query {
        getUser(email: String!): User
    }
`;

module.exports = {
    schema: schema,
};
