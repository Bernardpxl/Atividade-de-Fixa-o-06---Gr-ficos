import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")


df = pd.read_csv("dados_linhas.csv")
df["data"] = pd.to_datetime(df["data"])


plt.figure(figsize=(10, 5))
sns.lineplot(
    data=df, x="data", y="vendas", hue="loja", marker="o", palette="tab10"
)


plt.title(
    "Evolução Diária de Vendas por Loja", fontsize=14, fontweight="bold", pad=15
)
plt.xlabel("Data", fontsize=11)
plt.ylabel("Vendas (R$)", fontsize=11)
plt.xticks(rotation=45)
plt.legend(title="Loja")

plt.tight_layout()
plt.savefig("grafico_linhas.png", dpi=300)
plt.show()