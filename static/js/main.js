const iconThatChangesUserSettings = document.querySelector(".d-flex .fas");
const userSettings = document.querySelector(".user-settings");

try {
  iconThatChangesUserSettings.addEventListener("click", (e) => {
    userSettings.classList.toggle("display-setting");
  });
} catch (error) {
  error;
}

// GLIDER JS

try {
  const glider = new Glider(document.getElementById("glider"));
  sliderAuto(glider, 4000);
} catch (error) {
  // console.error(error, "Will check later");
}

function sliderAuto(slider, miliseconds) {
  const slidesCount = slider.track.childElementCount;
  let slideTimeout = null;
  let nextIndex = 1;

  function slide() {
    slideTimeout = setTimeout(function () {
      if (nextIndex >= slidesCount) {
        nextIndex = 0;
      }
      slider.scrollItem(nextIndex++);
    }, miliseconds);
  }

  slider.ele.addEventListener("glider-animated", function () {
    window.clearInterval(slideTimeout);
    slide();
  });

  slide();
}

// Tab Categories

const tabContents = document.querySelectorAll(".tab__content");
const categoryTabs = document.querySelectorAll(".category_tab");

categoryTabs.forEach((val) => {
  // console.log(val.textContent);
  val.addEventListener("mouseover", (e) => {
    e.preventDefault();
    let tabTitle = val.textContent;
    tabContents.forEach((tabContent) => {
      if (tabTitle.includes("All Categories")) {
        if (val.classList.contains("active-class")) {
          val.classList.remove("active-class");
        }

        if (
          tabContents[0].classList.contains("tab__active") ||
          tabContents[1].classList.contains("tab__active") ||
          tabContents[2].classList.contains("tab__active") ||
          tabContents[3].classList.contains("tab__active") ||
          tabContents[4].classList.contains("tab__active") ||
          tabContents[5].classList.contains("tab__active")
        ) {
          tabContents[0].classList.remove("tab__active");
          tabContents[1].classList.remove("tab__active");
          tabContents[2].classList.remove("tab__active");
          tabContents[3].classList.remove("tab__active");
          tabContents[4].classList.remove("tab__active");
          tabContents[5].classList.remove("tab__active");
        }
      } else if (tabTitle.includes("Clothing")) {
        if (tabContent.attributes.id.textContent === "cloth") {
          tabContent.classList.add("tab__active");
          if (
            tabContents[1].classList.contains("tab__active") ||
            tabContents[2].classList.contains("tab__active") ||
            tabContents[3].classList.contains("tab__active") ||
            tabContents[4].classList.contains("tab__active") ||
            tabContents[5].classList.contains("tab__active")
          ) {
            tabContents[1].classList.remove("tab__active");
            tabContents[2].classList.remove("tab__active");
            tabContents[3].classList.remove("tab__active");
            tabContents[4].classList.remove("tab__active");
            tabContents[5].classList.remove("tab__active");
          }
        }
      } else if (tabTitle.includes("Shoes")) {
        if (tabContent.attributes.id.textContent === "shoes") {
          tabContent.classList.add("tab__active");

          if (
            tabContents[0].classList.contains("tab__active") ||
            tabContents[2].classList.contains("tab__active") ||
            tabContents[3].classList.contains("tab__active") ||
            tabContents[4].classList.contains("tab__active") ||
            tabContents[5].classList.contains("tab__active")
          ) {
            tabContents[0].classList.remove("tab__active");
            tabContents[2].classList.remove("tab__active");
            tabContents[3].classList.remove("tab__active");
            tabContents[4].classList.remove("tab__active");
            tabContents[5].classList.remove("tab__active");
          }
        }
      } else if (tabTitle.includes("Food")) {
        if (tabContent.attributes.id.textContent === "food") {
          tabContent.classList.add("tab__active");

          if (
            tabContents[0].classList.contains("tab__active") ||
            tabContents[1].classList.contains("tab__active") ||
            tabContents[3].classList.contains("tab__active") ||
            tabContents[4].classList.contains("tab__active") ||
            tabContents[5].classList.contains("tab__active")
          ) {
            tabContents[0].classList.remove("tab__active");
            tabContents[1].classList.remove("tab__active");
            tabContents[3].classList.remove("tab__active");
            tabContents[4].classList.remove("tab__active");
            tabContents[5].classList.remove("tab__active");
          }
        }
      } else if (tabTitle.includes("Electronics")) {
        if (tabContent.attributes.id.textContent === "electronics") {
          tabContent.classList.add("tab__active");

          if (
            tabContents[0].classList.contains("tab__active") ||
            tabContents[1].classList.contains("tab__active") ||
            tabContents[2].classList.contains("tab__active") ||
            tabContents[4].classList.contains("tab__active") ||
            tabContents[5].classList.contains("tab__active")
          ) {
            tabContents[0].classList.remove("tab__active");
            tabContents[1].classList.remove("tab__active");
            tabContents[2].classList.remove("tab__active");
            tabContents[4].classList.remove("tab__active");
            tabContents[5].classList.remove("tab__active");
          }
        }
      } else if (tabTitle.includes("Home Appreance")) {
        if (tabContent.attributes.id.textContent === "home_appreance") {
          tabContent.classList.add("tab__active");

          if (
            tabContents[0].classList.contains("tab__active") ||
            tabContents[1].classList.contains("tab__active") ||
            tabContents[2].classList.contains("tab__active") ||
            tabContents[3].classList.contains("tab__active") ||
            tabContents[5].classList.contains("tab__active")
          ) {
            tabContents[0].classList.remove("tab__active");
            tabContents[1].classList.remove("tab__active");
            tabContents[2].classList.remove("tab__active");
            tabContents[3].classList.remove("tab__active");
            tabContents[5].classList.remove("tab__active");
          }
        }
      } else if (tabTitle.includes("Finance")) {
        if (tabContent.attributes.id.textContent === "finance") {
          tabContent.classList.add("tab__active");
          console.log(12333);
          if (
            tabContents[0].classList.contains("tab__active") ||
            tabContents[1].classList.contains("tab__active") ||
            tabContents[2].classList.contains("tab__active") ||
            tabContents[3].classList.contains("tab__active") ||
            tabContents[4].classList.contains("tab__active")
          ) {
            tabContents[0].classList.remove("tab__active");
            tabContents[1].classList.remove("tab__active");
            tabContents[2].classList.remove("tab__active");
            tabContents[3].classList.remove("tab__active");
            tabContents[4].classList.remove("tab__active");
          }
        }
      } else if (tabTitle.includes("Health Supplies")) {
        console.log("yes");
      }
    });
  });
});

// Ajax Code Goes Here

// CoverImage upload
uploadCoverImage();
function uploadCoverImage() {
  const coverImage = document.querySelector("#cover_image");
  const coverImageForm = document.querySelector("#cover_image_form");

  coverImage.addEventListener("click", (e) => {
    e.preventDefault();
    coverImageForm.classList.add("display_form_image");
  });
}

function getServerDataCategory(url) {
  axios.get(`${url}`);
}
