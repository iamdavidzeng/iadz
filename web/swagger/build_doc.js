const path = require('path');
const spectacle = require('spectacle-docs');


function resolvePath(fileName) {
    return path.resolve(__dirname, fileName);
}

spectacle({
    specFile: resolvePath('swagger.yaml'),
    targetDir: resolvePath('./dist'),
})
