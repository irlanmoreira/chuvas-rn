import pandas as pd

dados = pd.read_csv("dados/chuvas_rn.csv", parse_dates=["data"])
print(dados.groupby("municipio")["precipitacao_mm"].mean())
