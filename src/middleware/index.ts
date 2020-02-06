// type from https://github.com/gundam1993/kinopio/blob/master/lib/index.ts

import * as uuid from "uuid/v4";
import * as amqp from "amqplib";

interface EntrypointsHooks {
    processResponse?: (response: any) => any;
    onResponse?: (response: any) => void;
    onRequest?: (
        serviceName: string,
        functionName: string,
        rpcPayload: object
    ) => void;
}

