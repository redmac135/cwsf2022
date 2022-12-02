const summaries = {
  "Louis Wu": "Our first team member specializes in biology, behavioral sciences, and product design. He is a Remarkable Students Showcase Champion, won gold at the Canada-Wide Science Fair, and was chosen to represent Canada at the EU Contest for Young Scientists.",
  "Koral Kulacoglu": "Koral specializes in engineering, programming, and neural networks. Alongside Louis, Koral was one of the original developers of the FourSight project.",
  "Ethan Zhao": "Ethan specializes in web design and production. He manages website design, video editing, and video design.",
  "Alex Gan": "Alex specializes in finance, business management, and corporate development. Alex worked for the Ontario Public Service as a Finance & Risk Assistant and is now focused on corporate development of FourSight."
};

function getPerson(name) {
  let summary = summaries[name] ?? "Unknown Name";
  $('#modal-text').html(summary);
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
