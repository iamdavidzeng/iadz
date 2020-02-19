const io = require('socket.io')(3000)

const users = {}

io.on('connection', socket => {
    socket.on('new-user', ({room, name}) => {
        console.log(name + ' connected to ' + room);
        users[name] = socket
        socket.nickname = name
        socket.join(room);
        socket.broadcast.to(room).emit('user-connected', name);
    })
    socket.on('send-chat-message', ({room, message, name}) => {
        console.log(name + ' send: ' + message);
        socket.broadcast.to(room).emit('chat-message', { message: message, name })
    })
    socket.on('whisper', ({room, message, nickname}, callback) => {
        console.log('Whisper!')
        if (nickname in users) {
            users[nickname].emit('whisper', {name: socket.nickname, message})
            callback(message)
        } else {
            callback('Please enter a valid username.')
        }
    })
})
