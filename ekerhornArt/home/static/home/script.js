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
  let prevScrollPos = 0;

  // Check for first time visitor
  if (!localStorage.getItem("visited")) {
    localStorage.setItem("visited", "true");
  } else {
    // Select all objects with the css class "animate"
    const animated = document.querySelectorAll(".animate");
    // For each, add the letter "d" to the class
    animated.forEach((element) => {
      element.classList.add("animated");
    });
  }

  // BLUR LOAD
  const blurContainers = document.querySelectorAll(".blur-load");
  blurContainers.forEach((container) => {
    const img = container.querySelector("img");

    function loaded() {
      container.classList.add("loaded");
    }

    if (img.complete) {
      loaded();
    } else {
      img.addEventListener("load", loaded);
    }
  });

  // NAVBAR
  window.addEventListener("scroll", function () {
    const headerElement = document.getElementById("header");
    let currentScrollPos = window.scrollY;

    if (currentScrollPos == 0) {
      headerElement.style.background = "rgba(0, 0, 0, 0)";
      headerElement.style.boxShadow = "none";
      headerElement.style.borderBottom = "none";
    } else {
      headerElement.style.background = "var(--dark)";
      headerElement.style.boxShadow =
        "rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px";
      headerElement.style.borderBottom = "1px solid var(--a-dark)";
    }
    // If the user scrolls upwards, reveal the header
    if (currentScrollPos - prevScrollPos > 0 && currentScrollPos > 600) {
      headerElement.style.top = "-64px";
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

  // EVENTS

  // Get all event items
  const events = document.querySelectorAll(".item-container");

  // Loop through all event items
  events.forEach((event) => {
    // Function to handle the mouseover and touchstart events
    const hoverEvent = () => {
      // Remove any expanded class from all event items
      events.forEach((event) => {
        event.classList.remove("expanded");
      });

      // Find out which event item was hovered over or touched
      const hoveredEvent = event;
      // Readd the expanded class to the hovered event
      hoveredEvent.classList.add("expanded");
    };

    // Add event listeners for both mouseover and touchstart
    event.addEventListener("mouseover", hoverEvent);
    event.addEventListener("touchstart", hoverEvent);
  });

  // MODALS

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

  window.addEventListener("click", function (event) {
    // If user clicks outside of a modal, close it
    if (event.target.classList.contains("modal")) {
      event.target.close();
    }
  });
});
