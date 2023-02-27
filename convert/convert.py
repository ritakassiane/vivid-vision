import fitz
from PIL import Image

# Define a resolução da imagem PNG
dpi = 96  # define a resolução em pontos por polegada
resolution = (3840, 2160)  # define a resolução em pixels

# Abre o arquivo PDF
with fitz.open('vivid-vision.pdf') as doc:
    for i, page in enumerate(doc):
        # Renderiza a página como imagem rasterizada
        pixmap = page.get_pixmap(alpha=False)
        
        # Cria um objeto Image do Pillow a partir da imagem rasterizada
        img = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
        
        # Redimensiona a imagem para a resolução desejada
        img = img.resize(resolution)
        
        # Define o nome e o formato do arquivo PNG
        png_filename = f'pagina_{i}.png'
        
        # Salva a imagem PNG com a resolução definida
        img.save(png_filename, dpi=(dpi, dpi))
