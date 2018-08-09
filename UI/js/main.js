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