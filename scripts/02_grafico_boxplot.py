import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")


df = pd.read_csv("dados_boxplot.csv")


plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="departamento", y="salario", palette="Set2")


plt.title(
    "Distribuição Salarial por Departamento",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Departamento", fontsize=11)
plt.ylabel("Salário (R$)", fontsize=11)

plt.tight_layout()
plt.savefig("grafico_boxplot.png", dpi=300)
plt.show()