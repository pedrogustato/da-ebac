# código de geração do gráfico
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tabela = pd.read_csv("gasolina.csv")

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=tabela, x="dia", y="venda", palette="bright")
  grafico.set(title='Preço médio da Gasolina em SP - Julho/21', xlabel='Dia', ylabel='Preço médio (R$)');

grafico.legend(["Vendas"], loc='upper right', bbox_to_anchor=(1.1, 1))
