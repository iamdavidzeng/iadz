const io = require('socket.io')(3000)

const users = {}

io.on('connection', socket => {
    socket.on('new-user', (room, name) => {
        console.log(name + ' connected to ' + room);
        users[socket.id] = name
        socket.join(room);
        socket.broadcast.to(room).emit('user-connected', name);
    })
    socket.on('send-chat-message', (room, message) => {
        console.log(users[socket.id] + ' send: ' + message);
        socket.broadcast.to(room).emit('chat-message', { message: message, name: users[socket.id] })
    })
    socket.on('disconnect', () => {
        console.log(users[socket.id] + ' disconnected.')
        socket.broadcast.emit('user-disconnected', users[socket.id])
        delete users[socket.id]
    })
})
