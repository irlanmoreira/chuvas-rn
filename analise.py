import pandas as pd

dados = pd.read_csv("dados/chuvas_rn.csv")
print(dados.groupby("municipio")["precipitacao_mm"].mean())
