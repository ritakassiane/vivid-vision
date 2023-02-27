# 👁 Visão Vivida 
 
Este projeto se refere à versão web de um documento denominado Visão Vivida, do Natural English Institute. 

## ✏ Como editar o conteúdo?

Apenas a porção textual do projeto pode ser editada, e isso pode ocorrer de duas maneiras:

<li> <strong> Edite os textos presentes no index.html principal deste repositório: </strong> </li>

Essa opção é menos acessível a editores que não possuem conhecimentos básicos de HTML e CSS, visto que pode ser necessário ajustes de estilo para manter o padrão de  estilo desenvolvido.

<li> <strong> Edite o texto na versão <a href="https://drive.google.com/drive/folders/1GznZ17fjbdFFcdEsTBkaJnZ48xfXr0kI"> versão .pptx </a> </strong> </li>

Essa opção é completamente acessível a editores que não possuem conhecimentos básicos de HTML e CSS. Para que o conteúdo atualizado apareça na página desenvolvida, é necessário:

1. Exporte o arquivo pptx como um pdf. (Se seu PowerPoint não tiver essa opção, abra o aquivo com o Google Slide no navegador > Arquivo > Download > PDF)
2. Adicione o pdf gerado na pasta convert 
3. <a href="#convert"> Configure e rode o convert.py  </a> 



## <div id="convert">⚙ Configurando e Rodando o Convert</div>

O convert.py converte cada página de um arquivo PDF em imagens PNG de alta resolução (4k), utilizando Python 3.10.9 e as as bibliotecas PyMuPDF e Pillow. O usuário pode especificar o nome da pasta onde deseja salvar as imagens e o nome do arquivo PDF a ser convertido. As imagens PNG são salvas na pasta especificada com o nome "X.png", onde "X" é o número da página correspondente. 

As imagens geradas são adicionadas automaticamente à pagina, sem necessidade de edição do código HTML e CSS previamente desenvolvido. 

1. Faça o <a href="https://www.python.org/downloads/release/python-3109/">download</a> do python
2. Instale as dependencias do projeto rodando o comando "pip install -r requirements.txt" na raiz deste repositório
3. Na linha 38 do arquivo convert.py, altere o nome do arquivo pdf em questão para o nome do pdf que salvou ao exportar anteriormente
4. Rode o arquivo convert.py

