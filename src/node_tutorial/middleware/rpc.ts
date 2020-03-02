import { Kinopio } from "kinopio";
import { camelizeKeys } from "humps";
import acceptLanguage from "accept-language";
import { isString, toLower } from "lodash";


export const kinopio  = new Kinopio({
    hostname: process.env.RABBIT_SERVER,
    port: parseInt(process.env.RABBIT_PORT, 5672),
    vhost: process.env.RABBIT_VHOST,
    username: process.env.RABBIT_USER,
    password: process.env.RABBIT_PASS,
    processResponse: response => camelizeKeys(response),
    queuePrefix: "rpc.reply-cc-gateway",
});

acceptLanguage.languages([
    "en-us",
    "zh-cn",
    "en-gb",
])

export function namekoRpcContextMiddleware(req, _, next) {
    const workerCtx = {
        "nameko.call_id_stack": [req.callID],
    };

    if (req.auth) {
        workerCtx["nameko.authorization"] = req.auth;
    }

    const acceptLaguageHeader = req.get("Accept-Language");
    if (isString(acceptLaguageHeader)) {
        const language = toLower(acceptLanguage.get(acceptLaguageHeader));
        workerCtx["nameko.locale"] = language;
        workerCtx["nameko.language"] = language;
        req.locale = language;
    }

    req.rpc = kinopio.buildRpcProxy(workerCtx);
    console.log("rpc context:\n%j", workerCtx);

    next();
}