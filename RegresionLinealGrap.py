import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Generar datos de ejemplo
np.random.seed(0)
X = np.random.rand(100, 1) * 10  # Variable independiente (X)
y = 2 + 3 * X + np.random.randn(100, 1)  # Variable dependiente (y) con ruido

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predecir valores para el conjunto de prueba
y_pred = model.predict(X_test)

# Obtener los coeficientes del modelo
b0 = model.intercept_[0]  # Término independiente (intercepto)
b1 = model.coef_[0][0]    # Coeficiente de la variable independiente (pendiente)

# Imprimir los coeficientes
print(f"Intercepto (b0): {b0:.2f}")
print(f"Pendiente (b1): {b1:.2f}")

# Graficar los datos y la línea de regresión
plt.scatter(X_test, y_test, label='Datos de prueba')
plt.plot(X_test, y_pred, color='red', label='Línea de regresión')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regresión Lineal Simple')
plt.legend()
plt.show()