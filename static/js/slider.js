var expander = document.getElementById("expander");
expander.addEventListener("click", function () {
 var slider = document.getElementsByClassName("slider")[0];

  if (slider.classList.contains("slided")) {
    slider.classList.remove("slided");
  } else {
    slider.classList.add("slided");
  }

});
