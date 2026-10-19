import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")

df = pd.read_csv("dados_regressao.csv")


plt.figure(figsize=(8, 5))
sns.regplot(
    data=df,
    x="renda_mensal",
    y="gasto_mensal",
    color="darkred",
    scatter_kws={"alpha": 0.6},
    line_kws={"color": "navy"},
)


plt.title(
    "Regressão: Renda Mensal vs. Gasto Mensal",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Renda Mensal (R$)", fontsize=11)
plt.ylabel("Gasto Mensal (R$)", fontsize=11)

plt.tight_layout()
plt.savefig("grafico_regressao.png", dpi=300)
plt.show()