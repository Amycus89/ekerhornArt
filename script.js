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

  //Carousel
  const track = document.querySelector(".carousel-track");
  const slides = Array.from(track.children); // Makes an array of all items inside varialbe track
  const nextButton = document.querySelector("#nextBtn");
  const prevButton = document.querySelector("#prevBtn");
  const dotsNav = document.querySelector(".carousel-nav");
  const dots = Array.from(dotsNav.children);
  //Find the amount of slides
  const lastSlideIndex = slides.length - 1;

  const slideWidth = slides[0].getBoundingClientRect().width;

  // Arrange the slides next to one another
  slides.forEach((slide, index) => {
    slide.style.left = slideWidth * index + "px";
  });

  const moveToSlide = (track, currentSlide, targetSlide) => {
    track.style.transform = `translateX(-${targetSlide.style.left})`;
    currentSlide.classList.remove("current-slide");
    targetSlide.classList.add("current-slide");
  };

  const updateDots = (currentDot, targetDot) => {
    currentDot.classList.remove("current-slide");
    targetDot.classList.add("current-slide");
  };

  // Arrange the slides next to one another
  // When user clicks left, move slides to the left
  prevButton.addEventListener("click", (e) => {
    const currentSlide = track.querySelector(".current-slide");
    let prevSlide = currentSlide.previousElementSibling;
    const currentDot = dotsNav.querySelector(".current-slide");
    let prevDot = currentDot.previousElementSibling;
    // Find the index of the current slide
    const currentIndex = slides.indexOf(currentSlide);
    if (currentIndex === 0) {
      prevSlide = slides[lastSlideIndex];
      prevDot = dots[lastSlideIndex];
    }

    moveToSlide(track, currentSlide, prevSlide);
    updateDots(currentDot, prevDot);
  });
  // When user clicks right, move slides to the right
  nextButton.addEventListener("click", (e) => {
    const currentSlide = track.querySelector(".current-slide");
    let nextSlide = currentSlide.nextElementSibling;
    const currentDot = dotsNav.querySelector(".current-slide");
    let nextDot = currentDot.nextElementSibling;
    // Find the index of the current slide
    const currentIndex = slides.indexOf(currentSlide);
    if (currentIndex === lastSlideIndex) {
      nextSlide = slides[0];
      nextDot = dots[0];
    }

    moveToSlide(track, currentSlide, nextSlide);
    updateDots(currentDot, nextDot);
  });

  // When user clicks on a carousel-nav-btn, move slides to that slide
  dotsNav.addEventListener("click", (e) => {
    // What button was clicled on?
    const targetButton = e.target.closest("button"); // Only cares about buttons, returns null for anything else
    if (!targetButton) return; // If there is no button, eg value is null, return and exit the function
    const currentSlide = track.querySelector(".current-slide");
    const currentButton = dotsNav.querySelector(".current-slide");
    const targetIndex = dots.indexOf(targetButton); // Find the index of the button clicked
    const targetSlide = slides[targetIndex];
    moveToSlide(track, currentSlide, targetSlide);
    updateDots(currentButton, targetButton);
  });

  // Make modals in gallery section work

  // Get all modal buttons
  const modalButtons = document.querySelectorAll(".open-modal");
  // Get all modals
  const modals = document.querySelectorAll(".modal");
  // Get all modal close buttons
  const modalCloses = document.querySelectorAll(".close-modal");

  // Loop through all modal buttons, adding an event listener to each
  for (let i = 0; i < modalButtons.length; i++) {
    modalButtons[i].addEventListener("click", function () {
      modals[i].showModal();
    });
  }

  // Whenever the user clicks outside of a modal, close it
  window.addEventListener("click", function (event) {
    // If user clicks outside of a modal, close it
    if (event.target.classList.contains("modal")) {
      event.target.close();
    }
  });
});
