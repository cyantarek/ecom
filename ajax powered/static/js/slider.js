// You can also use "$(window).load(function() {"
$(document).ready(function () {
    // Slideshow 4
    $("#slider3").responsiveSlides({
        auto: true,
        pager: false,
        nav: true,
        speed: 500,
        namespace: "callbacks",
        before: function () {
            $('.events').append("<li>before event fired.</li>");
            alert("Hello");
        },
        after: function () {
            $('.events').append("<li>after event fired.</li>");
        }
    });

});
