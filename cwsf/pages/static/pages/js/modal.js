function getPerson(name) {
  url = `/api/person/${name}`;
  fetch(url, {
    format: 'json',
  })
    .then((response) => response.json())
    .then((data) => {
      let content = `${data.summary}`;
      $('#modal-text').html(content);
    })
    .catch((error) => {
      $('#modal-text').html('An internal error occurred. Try again later.');
    });
  $('#modal').show();
  $('#modal-content').css('opacity', '0');
  $('#modal-content').animate(
    {
      opacity: 1,
    },
    100
  );
}

function hideModal() {
  $('#modal').hide();
}

$(window).click(function (event) {
  if (event.target.id === 'modal') {
    hideModal();
  }
});
