"""
Análisis de Regresión Lineal - Cuarteto de Anscombe
Este script demuestra la implementación de regresión lineal en Python
para analizar los diferentes conjuntos de datos del Cuarteto de Anscombe.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings('ignore')

# Configuración de estilo para los gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class AnscombeAnalyzer:
    """Clase para analizar el Cuarteto de Anscombe con regresión lineal."""
    
    def __init__(self, data_path):
        """Inicializar el analizador con la ruta de los datos."""
        self.data = pd.read_csv(data_path)
        self.models = {}
        self.results = {}
        
    def load_data(self):
        """Cargar y preparar los datos."""
        print("Cargando datos del Cuarteto de Anscombe...")
        print(f"Forma de los datos: {self.data.shape}")
        print(f"Columnas: {list(self.data.columns)}")
        return self.data
    
    def calculate_descriptive_stats(self, x, y):
        """Calcular estadísticas descriptivas para un conjunto de datos."""
        stats = {
            'mean_x': np.mean(x),
            'var_x': np.var(x),
            'mean_y': np.mean(y),
            'var_y': np.var(y),
            'correlation': np.corrcoef(x, y)[0, 1],
            'r_squared': np.corrcoef(x, y)[0, 1] ** 2
        }
        return stats
    
    def fit_linear_regression(self, x, y):
        """Ajustar modelo de regresión lineal."""
        # Reshape para sklearn
        x_reshaped = x.values.reshape(-1, 1) if hasattr(x, 'values') else np.array(x).reshape(-1, 1)
        y_reshaped = y.values if hasattr(y, 'values') else np.array(y)
        
        # Crear y ajustar modelo
        model = LinearRegression()
        model.fit(x_reshaped, y_reshaped)
        
        # Predicciones
        y_pred = model.predict(x_reshaped)
        
        # Métricas
        r2 = r2_score(y_reshaped, y_pred)
        mse = mean_squared_error(y_reshaped, y_pred)
        
        return {
            'model': model,
            'predictions': y_pred,
            'r2': r2,
            'mse': mse,
            'coefficients': model.coef_[0],
            'intercept': model.intercept_
        }
    
    def analyze_dataset(self, dataset_num):
        """Analizar un conjunto específico de datos."""
        subset = self.data[self.data['group'] == dataset_num]
        x = subset['x']
        y = subset['y']
        
        print(f"\n{'='*50}")
        print(f"ANÁLISIS DEL CONJUNTO {dataset_num}")
        print(f"{'='*50}")
        
        # Estadísticas descriptivas
        stats = self.calculate_descriptive_stats(x, y)
        print(f"Media de X: {stats['mean_x']:.3f}")
        print(f"Varianza de X: {stats['var_x']:.3f}")
        print(f"Media de Y: {stats['mean_y']:.3f}")
        print(f"Varianza de Y: {stats['var_y']:.3f}")
        print(f"Correlación: {stats['correlation']:.3f}")
        print(f"R²: {stats['r_squared']:.3f}")
        
        # Regresión lineal
        regression_results = self.fit_linear_regression(x, y)
        print(f"Ecuación de regresión: Y = {regression_results['intercept']:.3f} + {regression_results['coefficients']:.3f}X")
        print(f"R² del modelo: {regression_results['r2']:.3f}")
        print(f"MSE: {regression_results['mse']:.3f}")
        
        # Guardar resultados
        self.models[dataset_num] = regression_results
        self.results[dataset_num] = {
            'stats': stats,
            'regression': regression_results
        }
        
        return subset, regression_results
    
    def create_visualizations(self):
        """Crear visualizaciones para todos los conjuntos de datos."""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Cuarteto de Anscombe - Análisis de Regresión Lineal', fontsize=16, fontweight='bold')
        
        for i in range(1, 5):
            subset = self.data[self.data['group'] == i]
            x = subset['x']
            y = subset['y']
            
            # Seleccionar subplot
            row = (i - 1) // 2
            col = (i - 1) % 2
            ax = axes[row, col]
            
            # Scatter plot
            ax.scatter(x, y, alpha=0.7, s=100, color=f'C{i-1}')
            
            # Línea de regresión
            if i in self.models:
                x_range = np.linspace(x.min(), x.max(), 100)
                y_pred = self.models[i]['intercept'] + self.models[i]['coefficients'] * x_range
                ax.plot(x_range, y_pred, 'r--', linewidth=2, alpha=0.8)
            
            # Configuración del subplot
            ax.set_title(f'Conjunto {i}', fontweight='bold')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.grid(True, alpha=0.3)
            
            # Añadir estadísticas al gráfico
            if i in self.results:
                r2 = self.results[i]['regression']['r2']
                ax.text(0.05, 0.95, f'R² = {r2:.3f}', transform=ax.transAxes, 
                       bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
        
        plt.tight_layout()
        plt.savefig('anscombe_regression_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def compare_datasets(self):
        """Comparar estadísticas entre los diferentes conjuntos."""
        print(f"\n{'='*60}")
        print("COMPARACIÓN DE ESTADÍSTICAS DESCRIPTIVAS")
        print(f"{'='*60}")
        
        comparison_data = []
        for i in range(1, 5):
            subset = self.data[self.data['group'] == i]
            stats = self.calculate_descriptive_stats(subset['x'], subset['y'])
            regression = self.results[i]['regression']
            
            comparison_data.append({
                'Conjunto': i,
                'Media X': stats['mean_x'],
                'Varianza X': stats['var_x'],
                'Media Y': stats['mean_y'],
                'Varianza Y': stats['var_y'],
                'Correlación': stats['correlation'],
                'R²': stats['r_squared'],
                'Intercepto': regression['intercept'],
                'Pendiente': regression['coefficients']
            })
        
        df_comparison = pd.DataFrame(comparison_data)
        print(df_comparison.round(3))
        
        return df_comparison
    
    def run_complete_analysis(self):
        """Ejecutar análisis completo del Cuarteto de Anscombe."""
        print("INICIANDO ANÁLISIS COMPLETO DEL CUARTETO DE ANSCOMBE")
        print("="*60)
        
        # Cargar datos
        self.load_data()
        
        # Analizar cada conjunto
        for i in range(1, 5):
            self.analyze_dataset(i)
        
        # Crear visualizaciones
        self.create_visualizations()
        
        # Comparar conjuntos
        comparison_df = self.compare_datasets()
        
        print(f"\n{'='*60}")
        print("CONCLUSIONES")
        print(f"{'='*60}")
        print("1. Todos los conjuntos tienen estadísticas descriptivas idénticas")
        print("2. Sin embargo, sus patrones visuales son completamente diferentes")
        print("3. Esto demuestra la importancia de la visualización de datos")
        print("4. Las estadísticas por sí solas pueden ser engañosas")
        print("5. Un análisis completo debe incluir tanto números como gráficos")
        
        return comparison_df

def main():
    """Función principal para ejecutar el análisis."""
    # Crear instancia del analizador
    analyzer = AnscombeAnalyzer('../data/df_anscombe.csv')
    
    # Ejecutar análisis completo
    results = analyzer.run_complete_analysis()
    
    # Guardar resultados en CSV
    results.to_csv('anscombe_comparison.csv', index=False)
    print(f"\nResultados guardados en 'anscombe_comparison.csv'")

if __name__ == "__main__":
    main()
