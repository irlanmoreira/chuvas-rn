# Chuvas RN
Análise exploratória das chuvas no Rio Grande do Norte.

## Como rodar
1. Instale as dependências: `pip install -r requirements.txt`
2. Calcule as médias: `python analise.py`
3. Avalie o modelo: `python avaliar.py`

## Avaliação do modelo
O `avaliar.py` compara as previsões com o que realmente aconteceu
(arquivo `dados/validacao.csv`) e mostra a acurácia.
