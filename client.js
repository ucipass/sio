var io = require('socket.io-client')
var socket = io.connect('http://localhost:8080', {reconnect: true});
socket.on('connect', function () {
    console.log("socket connected"); 
    echoLoop()
});

function echoLoop(){
    setInterval(()=>{
        socket.emit('echo', { user: 'me', msg: 'whazzzup?' }, (msg)=>{
            console.log("Received reply:",msg,new Date().toISOString())
        });
    },1000)
}