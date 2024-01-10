$(document).ready(function () {
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?';

    $('INPUT#btn_translate').on('click', function () {
      const languageCode = $('INPUT#language_code').val();

      $.get(apiUrl + $.param({ lang: languageCode }), function (data) {
        $('DIV#hello').text(data.hello);
      }).fail(function () {
        $('DIV#hello').text('Translation not available.');
      });
    });
  });
