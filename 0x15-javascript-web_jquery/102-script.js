$(document).ready(() => {
  $('#btn_translate').click(() => {
    const langCode = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${langCode}`, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
