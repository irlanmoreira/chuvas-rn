import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("dados/chuvas_rn.csv")
media = dados.groupby("municipio")["precipitacao_mm"].mean()
media.plot(kind="bar", title="Média de chuvas por município (mm)")
plt.tight_layout()
plt.savefig("grafico_chuvas.png")
