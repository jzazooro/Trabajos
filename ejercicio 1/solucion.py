### ¿POR QUE ESTAN BAJANDO LOS PRECIOS DE LOS COCHES? ¿MUESTRA SI LOS PRECIOS DE LOS COCHES ESTAN BAJANDO O NO?

# Importo librerias
import pandas as pd
import matplotlib.pyplot as plt

# Cargo los datos
df = pd.read_csv('ejercicio 1/test_data.csv')

# Convierto la columna 'day' a tipo datetime
df['day'] = pd.to_datetime(df['day'])

# Calculo el precio ponderado por número de coches vendidos
df['weighted_price'] = df['price'] * df['number_of_cars']
weighted_avg_price = df.groupby('day').apply(
    lambda x: x['weighted_price'].sum() / x['number_of_cars'].sum()
).reset_index(name='weighted_avg_price')

# Grafico la evolución del precio promedio ponderado
plt.figure(figsize=(12, 6))
plt.plot(weighted_avg_price['day'], weighted_avg_price['weighted_avg_price'], label='Precio Promedio Ponderado', color='green')
plt.title('Evolución del Precio Promedio Diario de Coches (Ponderado por Ventas)')
plt.xlabel('Fecha')
plt.ylabel('Precio Promedio Ponderado')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
