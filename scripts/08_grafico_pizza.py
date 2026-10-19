import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("dados_pizza.csv")


colors = sns.color_palette("pastel")[0 : len(df)]


plt.figure(figsize=(7, 7))
plt.pie(
    df["faturamento"],
    labels=df["canal_venda"],
    autopct="%1.1f%%",
    startangle=140,
    colors=colors,
    explode=[0.03] * len(df),
)


plt.title(
    "Distribuição do Faturamento por Canal de Venda",
    fontsize=14,
    fontweight="bold",
    pad=15,
)

plt.tight_layout()
plt.savefig("grafico_pizza.png", dpi=300)
plt.show()