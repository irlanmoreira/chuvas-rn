"""Avalia as previsões do modelo no conjunto de validação.

Uso: python avaliar.py [acuracia_minima]
"""
import csv
import sys

from config import LIMIAR


def acuracia(arquivo="dados/validacao.csv", limiar=LIMIAR):
    acertos = total = 0
    with open(arquivo, encoding="utf-8") as f:
        for linha in csv.DictReader(f):
            previu_chuva = float(linha["prob_chuva"]) >= limiar
            choveu = linha["choveu"] == "1"
            acertos += previu_chuva == choveu
            total += 1
    return acertos / total


if __name__ == "__main__":
    valor = acuracia()
    print(f"Acurácia: {valor:.2f}")
    minimo = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
    sys.exit(0 if valor >= minimo else 1)
