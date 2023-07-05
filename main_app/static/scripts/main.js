
$(".navbar-burger").click(function () {
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
});

$(".add-to-itinerary").click(function () {
    var destinationId = $(this).data("destination");
    $("#itinerary-dropdown-" + destinationId).toggleClass("show");
});
