#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# In[17]:


# Cargar el conjunto de datos desde la ruta local
archivo_csv = r'D:\VANESSA\Universidad_politecnico\Big DAta2\Anaisis_Datos_BigData\sales data-set.csv'
datos_ventas = pd.read_csv(archivo_csv)


# In[18]:


# Muestra el data frame
datos_ventas


# In[15]:


# Mostrar las primeras filas del conjunto de datos para verificar la carga correcta
print(datos_ventas.head())

# 2. Calcular estadísticas descriptivas
# Calculamos la media y la desviación estándar de las ventas semanales
media_ventas = datos_ventas['Weekly_Sales'].mean()
desviacion_estandar_ventas = datos_ventas['Weekly_Sales'].std()

print(f'Media de las ventas semanales: {media_ventas}')
print(f'Desviación estándar de las ventas semanales: {desviacion_estandar_ventas}')

# 3. Graficar los datos
plt.figure(figsize=(10, 6))
sns.histplot(datos_ventas['Weekly_Sales'], bins=20, kde=True)
plt.title('Distribución de Ventas Semanales')
plt.xlabel('Ventas Semanales')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()


# In[ ]:




