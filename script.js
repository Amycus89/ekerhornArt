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

    if (scrollTop === 0) {
      headerElement.style.backgroundColor = "initial";
      headerElement.style.color = "initial";
      headerElement.style.color = "white";
      headerElement.style.backgroundColor = "initial";
      headerElement.style.background =
        "linear-gradient(rgba(0, 0, 0, 1), rgba(0, 0, 0, 0))";
    } else {
      headerElement.style.color = "white";
      headerElement.style.background = neutralBlack;
    }
  });

  // OnClick hamburger icon animation and mobile navigation
  const hamburger = document.querySelector(".hamb");
  const mobileNav = document.querySelector(".sidebar");

  hamburger.addEventListener("click", function () {
    this.classList.toggle("active");
    mobileNav.classList.toggle("active");
  });

  // Whenever the width is smaller than 768px, close the mobile menu
});
