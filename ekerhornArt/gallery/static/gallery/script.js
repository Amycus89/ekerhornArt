let prevScrollPos = 0;
document.addEventListener("DOMContentLoaded", function () {
  window.addEventListener("scroll", function () {
    const headerElement = document.getElementById("header");
    let currentScrollPos = window.scrollY;
    //let scrollThreshold = 100;

    // If the user scrolls upwards, reveal the header
    if (currentScrollPos - prevScrollPos > 0 && currentScrollPos > 600) {
      headerElement.style.top = "-100px";
    } else {
      headerElement.style.top = "0";
    }
    prevScrollPos = currentScrollPos;
  });

  // OnClick hamburger icon animation and mobile navigation
  const hamburger = document.querySelector(".hamb");
  const mobileNav = document.querySelector(".sidebar");

  hamburger.addEventListener("click", function () {
    this.classList.toggle("active");
    mobileNav.classList.toggle("active");
  });

  // Whenever the width is smaller than 850px, close the mobile menu
  window.addEventListener("resize", function () {
    if (window.innerWidth > 850) {
      hamburger.classList.remove("active");
      mobileNav.classList.remove("active");
    }
  });
});
