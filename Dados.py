import pandas as pd 
import seaborn as sns   
import matplotlib.pyplot as plt 
from matplotlib import colormaps


df = pd.read_csv('ecommerce_estatistica.csv')
#print(df.head())
print(df.columns)
#GRAFICO DE HISTOGRAMA
plt.figure(figsize=(10, 6))
plt.hist(df['Nota'], bins=70, color='red', alpha=0.7)
plt.title('Histograma da Nota')
plt.xlabel('Nota')
plt.xticks(ticks=range(0, int(df['Nota'].max()) + 2, 10))
plt.ylabel('Frequência')
plt.grid(True)


#GRAFICO DE DISPERSÃO 
plt.figure(figsize=(10, 6))
plt.hexbin(df['Nota'], df['Preço'], gridsize=50, cmap='inferno', mincnt=1)
plt.title('Gráfico de Dispersão com Hexbin')
plt.xlabel('Nota')
plt.ylabel('Preço')
plt.grid(True)

#GRAFICO DE MAPA DE CALOR
plt.figure(figsize=(8, 5))
df_corr = df[['Nota', 'Preço', 'Desconto',]].corr()
sns.heatmap(df_corr, annot=True, cmap='plasma',fmt='.2f')
plt.title('Mapa de Calor da Correlação entre Nota, Preço e Desconto')

#GRAFICO DE BARRAS
plt.tight_layout() # Ajusta o layout para evitar sobreposição
plt.figure(figsize=(10, 6))
df['Nota'].value_counts().plot(kind='barh', cmap='plasma', alpha=0.7)
plt.title('GRAFICO DE BARRAS - Nota')
plt.xlabel('Quantidade')
plt.ylabel('Nota')
plt.xticks(rotation=45)


#GRAFICO DE PIZZA
plt.figure(figsize=(8, 8))
plt.pie(df['Temporada'].value_counts(), labels=df['Temporada'].unique(), autopct='%1.1f%%', startangle=180,)
plt.title('GRAFICO DE PIZZA - Temporada')
plt.tight_layout()


#GRAFICO DE DENSIDADE
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Nota'], fill=True, color="grey", alpha=0.7)
plt.xlabel('Nota')
plt.title('Gráfico de Densidade das Notas')


#GRAFICO DE REGRESSÃO
plt.figure(figsize=(8, 5))
sns.regplot(x='Nota', y='Preço', data=df, color='blue', marker='o', scatter_kws={'alpha':0.5, 'color' :'blue'}, line_kws={'color':'red'})
plt.title('Gráfico de Regressão entre Nota e Preço')



# plt.figure(figsize=(10, 6))
# plt.subplot(2, 2, 1)
# #Grafico de Dispersão das Notas
# plt.scatter(df['Nota'], df['Preço'], alpha=0.5, color='blue')
# plt.title('Gráfico de Dispersão das Notas')
# plt.xlabel('Nota')
# plt.ylabel('Preço')
# plt.grid(True)

# plt.subplot(1,2,2)
# plt.scatter(df['Nota'], df['Desconto'], alpha=0.5, cmap='plasma')
# plt.title('Gráfico de Dispersão das Notas')
# plt.xlabel('Nota')
# plt.ylabel('Desconto')

# corr= df[['Nota','Desconto']].corr()
# plt.subplot(2, 2, 3)
# sns.heatmap(corr, annot=True, cmap='plasma', cbar=True)
# plt.title('Correlação entre Nota e Desconto')

plt.show()




