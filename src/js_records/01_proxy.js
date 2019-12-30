const customizeProxy = (myCtx = { name: "david" }) => {
    return new Proxy(
        { myCtx },
        {
            get: (obj1, attr) => {
                // obj1 is `{ myCtx }` from upper layer.
                return new Proxy(
                    { attr },
                    {
                        get: (obj2, functionName) => {
                            // obj2 is `{ attr }` from upper layer.
                            return (payload) => {
                                console.log(obj1);
                                console.log(obj2);
                                console.log(functionName);
                                console.log(payload);
                                return 1;
                            }
                        }
                    }
                )
            }
        }
    )
}

const myProxy = customizeProxy();

console.log(myProxy);
console.log('#########');
console.log(myProxy.bookings);
console.log('#########');
console.log(myProxy.articles.get_article());
console.log('#########');
console.log(myProxy.users.get_user({args: [1, 2, 3]}));
