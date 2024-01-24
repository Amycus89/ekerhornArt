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

  window.addEventListener("scroll", function () {
    const headerElement = document.getElementById("header");
    let currentScrollPos = window.scrollY;
    //let scrollThreshold = 100;

    if (currentScrollPos == 0) {
      headerElement.style.backgroundColor = "initial";
      headerElement.style.color = "initial";
      headerElement.style.background =
        "linear-gradient(rgb(0, 0, 0), rgba(0, 0, 0, 0))";
      headerElement.style.boxShadow = "initial";
      headerElement.style.borderBottom = "none";
    } else {
      headerElement.style.background =
        "linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0)), linear-gradient(90deg, var(--dark), var(--a-dark), var(--dark))";
      headerElement.style.boxShadow =
        "rgba(50, 50, 93, 0.25) 0px 2px 5px -1px, rgba(0, 0, 0, 0.3) 0px 1px 3px -1px";
      headerElement.style.borderBottom = "1px solid var(--a-dark)";
    }
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
