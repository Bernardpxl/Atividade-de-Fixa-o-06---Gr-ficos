import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_theme(style="whitegrid")


df = pd.read_csv("dados_heatmap.csv")


dias_ordem = [
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sábado",
    "Domingo",
]
df["dia_semana"] = pd.Categorical(
    df["dia_semana"], categories=dias_ordem, ordered=True
)


pivot_heat = df.pivot(
    index="dia_semana", columns="horario", values="movimento_clientes"
)


plt.figure(figsize=(9, 6))
sns.heatmap(
    pivot_heat,
    annot=True,
    fmt="d",
    cmap="YlGnBu",
    cbar_kws={"label": "Nº de Clientes"},
)


plt.title(
    "Movimento de Clientes por Dia e Horário",
    fontsize=14,
    fontweight="bold",
    pad=15,
)
plt.xlabel("Horário", fontsize=11)
plt.ylabel("Dia da Semana", fontsize=11)

plt.tight_layout()
plt.savefig("grafico_heatmap.png", dpi=300)
plt.show()