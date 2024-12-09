import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
df = pd.read_csv('ventas_productos.csv')

# Calcular el precio total por producto
df['Precio Total'] = df['Cantidad'] * df['Precio']

# Crear un gráfico de barras
plt.bar(df['Producto'], df['Precio Total'])
plt.xlabel('Producto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Producto')

# Guardar el gráfico como imagen
plt.savefig('grafico_ventas.png')
plt.show()

print("Análisis completado. Gráfico guardado como 'grafico_ventas.png'.")
