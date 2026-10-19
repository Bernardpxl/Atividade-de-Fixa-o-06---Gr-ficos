import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")


df = pd.read_csv("dados_dispersao.csv")


plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="altura_cm",
    y="peso_kg",
    hue="sexo",
    style="sexo",
    s=70,
    palette="Set1",
)


plt.title(
    "Relação entre Altura e Peso", fontsize=14, fontweight="bold", pad=15
)
plt.xlabel("Altura (cm)", fontsize=11)
plt.ylabel("Peso (kg)", fontsize=11)
plt.legend(title="Sexo")

plt.tight_layout()
plt.savefig("grafico_dispersao.png", dpi=300)
plt.show()