import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
df = pd.read_csv('df_anscombe.csv')

print("=" * 50)
print("DESCRIPCIÓN ESTADÍSTICA DEL DATASET")
print("=" * 50)
print("\nDescribe() completo:")
print(df.describe())

print("\n" + "=" * 50)
print("Describe() por grupo:")
print("=" * 50)
for grupo in range(1, 5):
    print(f"\n--- Grupo {grupo} ---")
    print(df[df['group'] == grupo][['x', 'y']].describe())

# Crear gráficas de los 4 grupos
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Cuarteto de Anscombe - Los 4 Grupos', fontsize=16, fontweight='bold')

grupos = [1, 2, 3, 4]
posiciones = [(0, 0), (0, 1), (1, 0), (1, 1)]

for grupo, (i, j) in zip(grupos, posiciones):
    # Filtrar datos por grupo
    datos_grupo = df[df['group'] == grupo]
    
    # Hacer scatter plot
    axes[i, j].scatter(datos_grupo['x'], datos_grupo['y'], 
                       color=f'C{grupo-1}', s=100, alpha=0.6, edgecolors='black')
    
    # Agregar línea de regresión
    z = pd.DataFrame({'x': datos_grupo['x'], 'y': datos_grupo['y']})
    coef = z['x'].corr(z['y'])
    m, b = pd.Series(z['y']).cov(z['x']) / z['x'].var(), z['y'].mean() - (z['y'].cov(z['x']) / z['x'].var()) * z['x'].mean()
    axes[i, j].plot(datos_grupo['x'], m * datos_grupo['x'] + b, 
                    color='red', linestyle='--', linewidth=2, label=f'r={coef:.3f}')
    
    # Configurar el subplot
    axes[i, j].set_xlabel('X', fontsize=12)
    axes[i, j].set_ylabel('Y', fontsize=12)
    axes[i, j].set_title(f'Grupo {grupo}', fontsize=14, fontweight='bold')
    axes[i, j].grid(True, alpha=0.3)
    axes[i, j].legend()

plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print("Gráfica generada exitosamente!")
print("=" * 50)

