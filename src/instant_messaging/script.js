const messageContainer = document.getElementById('message-container')
const messageForm = document.getElementById('send-container')
const messageInput = document.getElementById('message-input')

const port = 3000
const socket = io(`http://localhost:${port}`)

const name = prompt('What is your name?')
const room = prompt('Type your room: ')
appendMessage('You joined ' + room)
socket.emit('new-user', {room, name});

socket.on('chat-message', data => {
    appendMessage(`${data.name}: ${data.message}`)
})

socket.on('user-connected', name => {
    appendMessage(`${name} connected`)
})

socket.on('user-disconnected', name => {
    appendMessage(`${name} disconnected`)
})

socket.on('whisper', data => {
    appendMessage(`${data.name}: ${data.message}`)
})

messageForm.addEventListener('submit', e => {
    e.preventDefault()
    var message = messageInput.value
    var index = message.indexOf(' ')
    if (index !== -1) {
        var nickname = message.substr(0, index)
        message = message.substr(index + 1)
        socket.emit('whisper', {room, message, nickname}, (data) => {
            appendMessage(`You: ${data}`)
        })
        messageInput.value = ''
    } else {
        appendMessage(`You: ${message}`)
        socket.emit('send-chat-message', {room, message, name})
        messageInput.value = ''
    }
})

function appendMessage(message) {
    const messageElement = document.createElement('div')
    messageElement.innerText = message
    messageContainer.append(messageElement)
}
