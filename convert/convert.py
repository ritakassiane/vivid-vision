import fitz
from PIL import Image
import os

# Define a resolução da imagem PNG
dpi = 96  # define a resolução em pontos por polegada
resolution = (3840, 2160)  # define a resolução em pixels

# Define o caminho da pasta onde as imagens serão salvas
folder_path = '../assets/images'

# Verifica se o caminho da pasta existe, caso contrário, cria a pasta
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

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
        png_filename = f'{i}.png'
        
        # Define o caminho completo do arquivo PNG
        png_filepath = os.path.join(folder_path, png_filename)
        
        # Salva a imagem PNG com a resolução definida e o caminho completo do arquivo
        img.save(png_filepath, dpi=(dpi, dpi))
