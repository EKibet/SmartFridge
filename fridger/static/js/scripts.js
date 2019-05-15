// Launch fullscreen
function launchIntoFullscreen(element) {
  if (element.requestFullscreen) {
    element.requestFullscreen();
  } else if (element.mozRequestFullScreen) {
    element.mozRequestFullScreen();
  } else if (element.webkitRequestFullscreen) {
    element.webkitRequestFullscreen();
  } else if (element.msRequestFullscreen) {
    element.msRequestFullscreen();
  }
}

$(".icon-fullscreen").on("click", function() {
  $(this).addClass("hide");
  launchIntoFullscreen(document.documentElement);
  $(".icon-exit-fullscreen").removeClass("hide");
  $(".grid-wrapper").css({
    height: "100vh"
  });
});

// Exit fullscreen
function exitFullscreen() {
  if (document.exitFullscreen) {
    document.exitFullscreen();
  } else if (document.mozCancelFullScreen) {
    document.mozCancelFullScreen();
  } else if (document.webkitExitFullscreen) {
    document.webkitExitFullscreen();
  }
}

$(".icon-exit-fullscreen").on("click", function() {
  $(this).addClass("hide");
  exitFullscreen(document.documentElement);
  $(".icon-fullscreen").removeClass("hide");
  $(".grid-wrapper").css({
    height: "90vh"
  });
});

$(".icon-menu").on("click", function() {
  $(".nav")
    .removeClass("hide")
    .addClass("fade-in");
  $(".icon-page-close").removeClass("hide");
});

$(".icon-menu-close").on("click", function() {
  $(".nav")
    .addClass("hide")
    .removeClass("fade-in");
  $(".icon-page-close").addClass("hide");
});

$(".icon-shop").on("click", function() {
  $("#shop")
    .removeClass("hide")
    .addClass("fade-in");
  $(".icon-page-close").removeClass("hide");
});

$(".logo").on("click", function() {
  $("#about")
    .removeClass("hide")
    .addClass("fade-in");
  $(".icon-page-close").removeClass("hide");
});

$(".icon-page-close").on("click", function() {
  $(".page, .icon-page-close").addClass("hide");
});

// menu links

$(".nav a").on("click", function() {
  var tabID = $(this).attr("data-tab");
  $(".icon-page-close, #" + tabID).removeClass("hide");
  $(".nav").addClass("hide");
});

// article links

$(".article-link").on("click", function() {
  var tabID = $(this).attr("data-tab");
  $(".icon-page-close, #" + tabID)
    .removeClass("hide")
    .addClass("fade-in");
});


