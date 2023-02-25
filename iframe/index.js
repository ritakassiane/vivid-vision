// Função para abrir a modal com o vídeo do YouTube
function openYoutubeModal(youtubeUrl) {
  // Define a URL do vídeo no iframe da modal
  var youtubeIframe = document.getElementById("youtubeIframe");
  youtubeIframe.src = youtubeUrl;

  // Abre a modal
  $("#youtubeModal").modal("show");
}

// Função para percorrer todos os links do PDF e adicionar um evento de clique para abrir a modal correspondente
function bindPdfLinks() {
  // Obtém todos os links no PDF
  var pdfLinks = document.querySelectorAll("a[href^='http://www.youtube.com']");

  // Adiciona o evento de clique a cada link
  for (var i = 0; i < pdfLinks.length; i++) {
    var pdfLink = pdfLinks[i];
    var youtubeUrl = pdfLink.href;

    pdfLink.onclick = function (event) {
      event.preventDefault();
      openYoutubeModal(youtubeUrl);
    };
  }
}

// Espera o documento estar pronto antes de adicionar o evento de clique nos links do PDF
$(document).ready(function () {
  bindPdfLinks();
});
