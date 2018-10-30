

var check1 = document.querySelector("input[name=LED1]");
var check2 = document.querySelector("input[name=LED2]");
var check3 = document.querySelector("input[name=LED3]");

check1.addEventListener('change', function(){
    console.log("LED1 set to " + this.checked);
});

check2.addEventListener('change', function(){
    console.log("LED2 set to " + this.checked);
});

check3.addEventListener('change', function(){
    console.log("LED3 set to " + this.checked);
});