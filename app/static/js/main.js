const lis = document.querySelectorAll(".column li");
const a = document.querySelectorAll("li a");
for (let i = 0; i < lis.length; i++) {
    
  lis[i].addEventListener("click", function() {
    for (let i = 0; i < lis.length; i++) {
      lis[i].classList.remove("sidebar-items__nav--active");
      a[i].classList.remove("active-text");
    }
    this.classList.add("sidebar-items__nav--active");
    a[i].classList.add("active-text");
  });
}


const stats = document.querySelectorAll('.stats-box');
const vote = document.querySelectorAll('.votes');
const thumb = document.querySelectorAll('.vote_thumb');
var count;

// add events to selector
for (let i = 0; i < stats.length; i++) {    
  thumb[i].addEventListener("click", function() {
    vote[i].classList.remove("fadeIn");

    // Increment with some fadin animation
    setTimeout(function(){
      vote[i].classList.add("fadeIn");
      count = vote[i].innerText;
      vote[i].innerHTML = parseInt(count) + 1;
      vote[i].classList.add("active-text");
    }, 300); 
        
  });
}