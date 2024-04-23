window.onscroll = function() {myFunction()};

function myFunction() {
  if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
    document.getElementById("navbar").style.backgroundColor= "black";
  } else {
    document.getElementById("navbar").style.backgroundColor = "transparent";
  }
}

document.addEventListener("DOMContentLoaded", (event) => {
  if(window.location.href=="http://127.0.0.1:8000/about/")
    document.getElementById("content").innerHTML="EXPERIENCE THE ESSENCE OF BEAUTY WITH SKIN-SAVIOUR";
  else if(window.location.href=="http://127.0.0.1:8000/quiz/")
    document.getElementById("content").innerHTML="TAKE OUR SKIN QUIZ TO RECEIVE EXPERT INSIGHTS";
  else if(window.location.href=="http://127.0.0.1:8000/skin_treatment/")
    document.getElementById("content").innerHTML="SKIN TREATMENT";
  else if(window.location.href=="http://127.0.0.1:8000/tips/")
    document.getElementById("content").innerHTML="TIPS";
  else if(window.location.href=="http://127.0.0.1:8000/contact_us/")
    document.getElementById("content").innerHTML="STAY CONNECTED WITH US FOR MORE SKINCARE INSIGHTS";

    document.addEventListener("click",()=>{
      var element=document.getElementById("dropdown");
      var element1=document.getElementById("dropdown1");
      var ham_content1=document.getElementById("tabs-hamburger");
      ham_content1,style.display="none";
      element.style.display="none";
      element1.style.display="none";
    })
});


// profile dropdown

var dropdown=document.getElementById("profile");
var dropdown1=document.getElementById("profile1");
dropdown.addEventListener("click",(event)=>{
  event.stopPropagation()
  var element=document.getElementById("dropdown");
  if(element.style.display=="block"){
    element.style.display="none";
  }
  else{
    element.style.display="block";
  }
  
})
dropdown1.addEventListener("click",(event)=>{
  event.stopPropagation()
  var element=document.getElementById("dropdown1");
  if(element.style.display=="block"){
    element.style.display="none";
  }
  else{
    element.style.display="block";
  }
  
})
  


function logout(event){
  var overlay = document.getElementById('overlay');
    var popup = document.getElementById('popup');
    var child=document.createElement("p");
    var timer=document.createElement("div");


    child.classList.add("loginerror");
    timer.classList.add("timer-bar")
    child.innerText="successfully logged out";
    popup.appendChild(child);
    child.appendChild(timer);
    overlay.style.display = 'block';


    var width=100;
    timerInterval= setInterval(function () {
    width = width-3;
    timer.style.width = width + '%';
    }, 100);


    setTimeout(()=>{
        overlay.style.display = 'none';
        clearInterval(timerInterval);
    }, 3000)
}


// Hamburger

var hamburger=document.getElementById("hamburger");
var ham_content=document.getElementById("tabs-hamburger");

hamburger.addEventListener("click",(event)=>{
  event.stopPropagation()
  if(ham_content.style.display=="none"){
    ham_content.style.display="block";
  }
  else{
    ham_content.style.display="none";
  }
})