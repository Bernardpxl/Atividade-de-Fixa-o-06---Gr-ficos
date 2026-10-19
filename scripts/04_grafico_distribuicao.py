import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")


df = pd.read_csv("dados_distribuicao.csv")


plt.figure(figsize=(8, 5))
sns.histplot(df["idade"], kde=True, bins=15, color="teal")


plt.title(
    "Distribuição de Idade dos Clientes", fontsize=14, fontweight="bold", pad=15
)
plt.xlabel("Idade (Anos)", fontsize=11)
plt.ylabel("Frequência Absoluta", fontsize=11)

plt.tight_layout()
plt.savefig("grafico_distribuicao.png", dpi=300)
plt.show()