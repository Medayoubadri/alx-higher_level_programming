$(document).ready(() => {
  function translateHello () {
    const langCode = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, (data) => {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(translateHello);

  $('#language_code').keypress((e) => {
    if (e.which == 13) {
      // Enter key
      translateHello();
    }
  });
});
