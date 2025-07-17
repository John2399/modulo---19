
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lendo os dados
df = pd.read_csv("gasolina.csv")

# Criando o gráfico
plt.figure(figsize=(10,6))
sns.lineplot(x="dia", y="venda", data=df)
plt.title("Preço médio da gasolina na cidade de São Paulo - Julho 2021")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.grid(True)

# Salvando o gráfico
plt.savefig("gasolina.png")
