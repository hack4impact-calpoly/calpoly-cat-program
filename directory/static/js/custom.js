// custom JS for this project

jQuery(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});

$('#list').click(function() {
    $('#grid').button('toggle');
    $('#cat_grid').attr('style','display:none !important');
    $('#cat_list').attr('style','');
});

$('#grid').click(function() {
    $('#list').button('toggle');
    $('#cat_grid').attr('style','');
    $('#cat_list').attr('style','display:none !important');
});

// search function

$.expr[":"].contains = $.expr.createPseudo(function(arg) {
    return function( elem ) {
        return $(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
    };
});

$('#search').keyup(function() {
    // will result in the first half being cards, second being list view
    let hide = $(".name:not(:contains('" + this.value + "'))");
    let show = $(".name:contains('" + this.value + "')");

    $("#result_count").text(show.length / 2);

    for (let i = 0; i < hide.length / 2; i++)
        $(hide[i]).closest(".fake-card").attr('style','display:none !important');

    for (let i = hide.length / 2; i < hide.length; i++)
        $(hide[i]).closest("li").attr('style','display:none !important');

    for (let i = 0; i < show.length / 2; i++)
        $(show[i]).closest(".fake-card").attr('style', '');

    for (let i = show.length / 2; i < show.length; i++)
        $(show[i]).closest("li").attr('style','');
});
