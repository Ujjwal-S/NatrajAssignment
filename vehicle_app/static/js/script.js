let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let accordionBtn = document.querySelector("#accordion");
let accordionContent = document.getElementsByClassName("accordion-content")[0]

closeBtn.addEventListener("click", () => {
  sidebar.classList.toggle("open");
  menuBtnChange();
});

function menuBtnChange() {
  if (sidebar.classList.contains("open")) {
    closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
  } else {
    closeBtn.classList.replace("bx-menu-alt-right", "bx-menu");
    accordionContent.style.display = "none";
  }
}

accordionBtn.addEventListener("click", () => {
  accordionBtn.classList.toggle("accordion-active");
  accordionContentHandeler()
})
function accordionContentHandeler() {
  let accordion_class_list = accordionBtn.classList
  for (let i = 0; i < accordion_class_list.length; ++i) {
    if (accordion_class_list[i] === "accordion-active") {
      accordionContent.style.display = "block";
      return;
    }
  }
  accordionContent.style.display = "none";
}