$(document).ready(function(){

    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');

    socket.on('mode', function(event) {
        $('body').append(event.data + '<br>');
        socket.emit('keepalive', {data: 'Keep alive request'});
    });

    socket.on('connection'), function(event) {
        console.log('Connected to server');
    }

    $('.currentface').click(function(event) {
        socket.emit('getcurrentface');
        return false;
    });
});