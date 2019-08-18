const resolvers =  {
    Query: {
        getUser: async (_, { email }, { rpc }) => {

            try {
                const user = await rpc.users.get_user({
                    kwargs: { email }
                });
                return user;
            } catch(error) {
                console.log(error);
            }
        },
    },
};


module.exports = {
    resolvers: resolvers,
};
