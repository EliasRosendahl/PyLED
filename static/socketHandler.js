var socket = io.connect('http://' + document.domain + ':' + location.port);


var check1 = document.querySelector("input[name=LED1]");
var check2 = document.querySelector("input[name=LED2]");
var check3 = document.querySelector("input[name=LED3]");

function getData(){
    var data = [];
    data.push(check1.checked);
    data.push(check2.checked);
    data.push(check3.checked);
    return data;
}

check1.addEventListener('change', function(){
    console.log("LED1 set to " + this.checked);
    socket.emit('setLED', getData());
});

check2.addEventListener('change', function(){
    console.log("LED2 set to " + this.checked);
    socket.emit('setLED', getData());

});

check3.addEventListener('change', function(){
    console.log("LED3 set to " + this.checked);
    socket.emit('setLED', getData());
});