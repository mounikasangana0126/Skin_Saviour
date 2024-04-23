var popup=document.getElementById("popup");
if(popup){

    var overlay = document.getElementById('overlay');
    var child=document.getElementById("message");
    var timer=document.createElement("div");
    
    
    timer.classList.add("timer-bar")
    child.appendChild(timer);
    overlay.style.display = 'block';
    popup.style.display = 'flex';


    var width=100;
    timerInterval= setInterval(function () {
    width = width-2;
    timer.style.width = width + '%';
    }, 100);


    setTimeout(()=>{
        popup.style.display="none";
        overlay.style.display = 'none';
        clearInterval(timerInterval);
    }, 5000)
}