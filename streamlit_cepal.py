import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns

# Ruta a la imagen
ruta_imagen = "C:\JHAA\CEPAL_2\CEPAL.jpg"

# Función para cargar y mostrar la imagen
def cargar_imagen(ruta):
    imagen = Image.open(ruta)
    return imagen

# Título de la aplicación
st.title('CEPAL - INDICADORES ODS-CORR')

# Cargar y mostrar la imagen
imagen = cargar_imagen(ruta_imagen)
st.image(imagen, caption='Imagen "CEPAL"', use_column_width=True)



# Ruta al archivo CSV
ruta_csv = r'C:\JHAA\CEPAL_2\reduced_df.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(ruta_csv)

# Obtener la lista de columnas disponibles para el menú desplegable
columnas_disponibles = list(df.columns)
columnas_disponibles.remove('Year')  # Remover la columna 'Year' de las opciones de columna Y

# Crear el menú desplegable para seleccionar las columnas Y
columnas_seleccionadas = st.sidebar.multiselect('Selecciona las columnas para Y', columnas_disponibles)

# Crear el menú desplegable para seleccionar un país
pais_seleccionado = st.sidebar.selectbox('Selecciona un país', df['Country'].unique())

# Filtrar el DataFrame por país
df_filtrado = df[df['Country'] == pais_seleccionado]

# Crear la gráfica de líneas utilizando Matplotlib y Streamlit
plt.figure(figsize=(10, 6))
for columna in columnas_seleccionadas:
    plt.plot(df_filtrado['Year'], df_filtrado[columna], marker='o', label=columna)
plt.title(f'Gráfica para {pais_seleccionado}')
plt.xlabel('Year')
plt.legend()
st.pyplot(plt)


# Ruta al archivo CSV
ruta_csv = r'C:\JHAA\CEPAL_2\reduced_df.csv'

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(ruta_csv)

# Obtener las columnas que contienen ODS y CRP
columnas_ods = [col for col in df.columns if 'ODS' in col]
columnas_crp = [col for col in df.columns if 'CRP' in col]

# Crear menús desplegables para seleccionar las variables ODS y CRP
ods_seleccionado = st.sidebar.selectbox('Selecciona una variable ODS', columnas_ods)
crp_seleccionado = st.sidebar.selectbox('Selecciona una variable CRP', columnas_crp)

# Graficar la correlación entre las variables seleccionadas
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x=ods_seleccionado, y=crp_seleccionado)
plt.title(f'Correlación entre {ods_seleccionado} y {crp_seleccionado}')
plt.xlabel(ods_seleccionado)
plt.ylabel(crp_seleccionado)
st.pyplot(plt)
