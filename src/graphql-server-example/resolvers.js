const resolvers =  {
    Query: {
        me: () => {
            return { username: "David Zeng" };
        }
    },
};


module.exports = {
    resolvers: resolvers,
};
