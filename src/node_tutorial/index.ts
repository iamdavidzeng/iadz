import * as express from "express";

const app = express();
const port = 8081;

function myLogger(_, __, next) {
    console.log("LOGGED");
    next();
}

function requestTime(req, _, next) {
    req.requestTime = Date().toString()
    next();
}

app.use(myLogger);
app.use(requestTime);

app.get("/", (req, res) => {
    let responseText = "Hello, world!<br>"
    responseText += req.requestTime
    res.send(responseText);
})

app.listen(port, () => {
    console.log(`Server started at http://localhost:${ port }`);
});
