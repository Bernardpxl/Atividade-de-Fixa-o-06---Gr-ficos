import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")


df = pd.read_csv("dados_frequencia.csv")


plt.figure(figsize=(8, 5))
ax = sns.countplot(
    data=df,
    x="tipo_atendimento",
    palette="viridis",
    order=df["tipo_atendimento"].value_counts().index,
)


for p in ax.patches:
  ax.annotate(
      f"{int(p.get_height())}",
      (p.get_x() + p.get_width() / 2.0, p.get_height()),
      ha="center",
      va="center",
      xytext=(0, 5),
      textcoords="offset points",
      fontsize=10,
  )


plt.title(
    "Frequência de Chamados por Tipo de Atendimento",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Tipo de Atendimento", fontsize=11)
plt.ylabel("Quantidade de Chamados", fontsize=11)

plt.tight_layout()
plt.savefig("grafico_frequencia.png", dpi=300)
plt.show()