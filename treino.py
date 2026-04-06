import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from config import N_ARVORES

dados = pd.read_csv("dados/historico_natal.csv")
X = dados[["umidade", "pressao", "temperatura"]]
y = dados["choveu"]
modelo = RandomForestClassifier(n_estimators=N_ARVORES, random_state=42).fit(X, y)
print("Acurácia no treino:", modelo.score(X, y))
