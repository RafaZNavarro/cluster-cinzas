# Processamento de Imagens: Redução de Tons de Cinza

Este projeto demonstra técnicas de processamento de imagens para converter imagens coloridas em tons de cinza e reduzir a quantidade de tons de cinza.

## Funcionalidades Principais

- Conversão de imagens coloridas para tons de cinza
- Redução de tons de cinza (de 256 para 64 tons)
- Geração de histogramas comparativos
- Visualização lado a lado das imagens
- Salvamento automático das imagens processadas

## Requisitos

- Python 3.6+
- Bibliotecas: Pillow, NumPy, Matplotlib

Instale as dependências com:
pip install pillow numpy matplotlib

## Como Usar

1. Coloque sua imagem na pasta do projeto
2. Modifique a variável caminho-imagem no código na linha 64
3. Execute o script

## Saídas do Programa

1. Arquivos gerados:
   - imagem_256.jpg: Imagem em tons de cinza (256 tons)
   - imagem_64.jpg: Imagem com tons reduzidos (64 tons)

2. Visualizações:
   - Comparação das três imagens (colorida, cinza e reduzida)
   - Histogramas comparando a distribuição de tons

## Explicação Técnica

Processo de Redução de Tons:
- Agrupa blocos de 4 tons em um único tom
- Usa o valor central do grupo como representante
- Exemplo: Tons 0-3 → Tom 2, Tons 4-7 → Tom 6

## Personalização

Modifique o parâmetro grupo para diferentes níveis:
- grupo=2: 128 tons
- grupo=8: 32 tons
- grupo=16: 16 tons