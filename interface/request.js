$(document).ready(function() {
  $("#r1").click(function() {
    $("#result-text").html("oui");
    // $.get("/get-string1", function(data) {
    //   $("#result-text").html(data);
    // });
  });

  $("#r2").click(function() {
    $.get("/get-string2", function(data) {
      $("#result-text").html(data);
    });
  });

  $("#r3").click(function() {
    $.get("/get-string3", function(data) {
      $("#result-text").html(data);
    });
  });
});
