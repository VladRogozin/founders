let greeting = document.querySelector(".hhh");
let direction = 1;
let offset = 0;

setInterval(() => {
    offset += direction * 5;
    if (offset > 20 || offset < 0) direction *= -1;
    greeting.style.top = offset + "px";
}, 2000);

