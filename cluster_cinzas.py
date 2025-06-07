# %%
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# %%
def carregar_imagem_colorida(imagem_path):
    return Image.open(imagem_path)

def converter_para_cinza(imagem_colorida):
    return imagem_colorida.convert("L")

def agrupar_tons_cinza(imagem_array, grupo=4):
    imagem_agrupada = (imagem_array // grupo) * grupo + grupo // 2
    return imagem_agrupada.astype(np.uint8)

def salvar_imagem(imagem_array, path_saida):
    imagem = Image.fromarray(imagem_array)
    imagem.save(path_saida)

def plotar_histogramas(imagem_cinza_np, imagem_agrupada_np):
    plt.figure(figsize=(12, 5))

    # Histograma da imagem original em cinza (256 tons)
    plt.subplot(1, 2, 1)
    plt.hist(imagem_cinza_np.flatten(), bins=256, color='gray', edgecolor='black')
    plt.title('Histograma - Tons de Cinza (256)')
    plt.xlabel('Intensidade de Cinza')
    plt.ylabel('Frequência')

    # Histograma da imagem agrupada (64 tons)
    plt.subplot(1, 2, 2)
    plt.hist(imagem_agrupada_np.flatten(), bins=64, color='gray', edgecolor='black')
    plt.title('Histograma - Tons Agrupados (64)')
    plt.xlabel('Intensidade de Cinza')
    plt.ylabel('Frequência')

    plt.tight_layout()
    plt.show()


def exibir_imagens(colorida, cinza, agrupada):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    
    axs[0].imshow(colorida)
    axs[0].set_title('Imagem Original (Colorida)')
    axs[0].axis('off')
    
    axs[1].imshow(cinza, cmap='gray')
    axs[1].set_title('Convertida para Tons de Cinza')
    axs[1].axis('off')
    
    axs[2].imshow(agrupada, cmap='gray')
    axs[2].set_title('Tons de Cinza Agrupados (64)')
    axs[2].axis('off')
    
    plt.tight_layout()
    plt.show()



# %%
## Caminho da imagem original
imagem_path = "caminho-imagem"  # Substitua pelo caminho da imagem

# Processamento
imagem_colorida = carregar_imagem_colorida(imagem_path)
imagem_cinza = converter_para_cinza(imagem_colorida)
imagem_cinza_np = np.array(imagem_cinza)
imagem_agrupada = agrupar_tons_cinza(imagem_cinza_np, grupo=4)

# Salvar imagem agrupada
salvar_imagem(imagem_cinza_np, "imagem_256.jpg")
salvar_imagem(imagem_agrupada, "imagem_64.jpg")

# Exibir as imagens
exibir_imagens(imagem_colorida, imagem_cinza, imagem_agrupada)



# %%
plotar_histogramas(imagem_cinza_np, imagem_agrupada)


