import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Categoría': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Frecuencia': [40, 30, 20, 15, 10, 8, 6, 4, 2, 1]
}
df = pd.DataFrame(data)

df_sorted = df.sort_values(by='Frecuencia', ascending=False)
df_sorted['Porcentaje'] = df_sorted['Frecuencia'] / df_sorted['Frecuencia'].sum() * 100
df_sorted['Acumulado'] = df_sorted['Porcentaje'].cumsum()

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.bar(df_sorted['Categoría'], df_sorted['Frecuencia'], color='skyblue')
ax1.set_xlabel('Categoría')
ax1.set_ylabel('Frecuencia', color='skyblue')
ax1.tick_params(axis='y', labelcolor='skyblue')

ax2 = ax1.twinx()
ax2.plot(df_sorted['Categoría'], df_sorted['Acumulado'], color='red', marker='D', ms=7)
ax2.set_ylabel('Porcentaje Acumulado (%)', color='red')
ax2.tick_params(axis='y', labelcolor='red')

plt.title('Diagrama de Pareto')
plt.show()