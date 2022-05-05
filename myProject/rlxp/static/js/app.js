$(document).foundation()

function overlayAssignmentForm(){
  console.log("assignment");
  el = document.getElementById("overlayAssignmentForm");
  el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}

function overlayChoreForm(){
  console.log("chore");
  el = document.getElementById("overlayChoreForm");
  el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}