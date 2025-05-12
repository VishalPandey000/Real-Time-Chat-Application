const socket = io();
let username, room;

function joinRoom() {
    username = document.getElementById('username').value;
    room = document.getElementById('room').value;
    socket.emit('join', { username, room });
}

function sendMessage() {
    let message = document.getElementById('message').value;
    socket.emit('message', { username, message });
    document.getElementById('message').value = '';
}

socket.on('message', data => {
    let chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p>${data}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight;
});
