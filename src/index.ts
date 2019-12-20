import * as express from "express";

const app = express();
const port = 8080;

app.get("/", (_req, res) => {
    res.send("Hello, world!");
})

app.listen(port, () => {
    console.log(`Server started at http://localhost:${ port }`);
});
