$(document).ready(function () {
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
        $.each(data.results, function (i, movie) {
            $('<li>').text(movie.title).appendTo('UL#list_movies');
        });
    });
});
