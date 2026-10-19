import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Configuração de estilo
sns.set_theme(style="whitegrid")


df = pd.read_csv("dados_barras.csv")


plt.figure(figsize=(9, 5))
sns.barplot(
    data=df, x="categoria", y="vendas_medias", hue="regiao", palette="Blues_r"
)


plt.title(
    "Vendas Médias por Categoria e Região",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Categoria de Produto", fontsize=11)
plt.ylabel("Vendas Médias (R$)", fontsize=11)
plt.legend(title="Região", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout()
plt.savefig("grafico_barras.png", dpi=300)
plt.show()