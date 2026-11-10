import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("dados/chuvas_rn.csv", parse_dates=["data"])
mensal = dados.groupby(dados["data"].dt.month)["precipitacao_mm"].sum()
mensal.plot(kind="line", marker="o", title="Chuva total por mês (mm)")
plt.xlabel("Mês")
plt.tight_layout()
plt.savefig("grafico_mensal.png")
