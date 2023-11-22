document.addEventListener("DOMContentLoaded", function () {
  // Change styling of navbar based on scroll
  const primaryLight = "#eaeff0";
  const primaryNormal = "#6e7fa1";
  const primaryDark = "#101b30";
  const accentDark = "#c8a872";
  const accentHover = "#e3c797";
  const accentNormal = "#e8d0ab";
  const neutralLight = "#f6f7f8";
  const neutralNormal = "#e3e5eb";
  const neutralBlack = "#00040d";

  window.addEventListener("scroll", function () {
    const headerElement = document.getElementById("header");
    let scrollTop = window.scrollY || document.documentElement.scrollTop;

    if (scrollTop < 20) {
      headerElement.style.backgroundColor = "initial";
      headerElement.style.color = "initial";
      headerElement.style.backgroundColor = "initial";
      headerElement.style.background =
        "linear-gradient(rgba(0, 0, 0, 1), rgba(0, 0, 0, 0))";
      headerElement.style.boxShadow = "initial";
    } else {
      headerElement.style.background = neutralBlack;
      headerElement.style.boxShadow =
        "rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px";
    }
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
