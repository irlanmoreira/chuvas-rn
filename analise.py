import pandas as pd

dados = pd.read_csv("dados/chuvas_rn.csv", parse_dates=["data"])
print(dados.groupby("municipio")["precipitacao_mm"].mean())

# Média mensal de chuvas por município
mensal = dados.groupby(["municipio", dados["data"].dt.month])["precipitacao_mm"].mean()
print(mensal)
