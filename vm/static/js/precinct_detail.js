$(document).ready(function() {
    $('.individual-voter').mouseenter(function() {
        $('.individual-voter').removeClass("voter_highlight");
        $(this).addClass("voter_highlight");
    });

    $(".individual-voter").mouseleave(function() {
        $(this).removeClass("voter_highlight");
    });
});
