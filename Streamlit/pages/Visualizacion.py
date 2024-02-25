import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Título e introducción
st.title("Visualización de Datos de Accidentes de Tráfico")
st.markdown("En esta sección, se presentan visualizaciones y análisis de datos relacionados con los accidentes de tráfico.")

# Cargar los datos
url_homicidios = "https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/homicidios.xlsx"
hechos = pd.read_excel(url_homicidios)

# Mostrar dataset
if st.checkbox("Mostrar dataset"):
    st.write(hechos)

# Mostrar head o tail del dataset
if st.checkbox("Ver las primeras o últimas filas del dataset"):
    option = st.radio("Seleccione una opción:", ("Head", "Tail"))
    if option == "Head":
        st.write(hechos.head())
    elif option == "Tail":
        st.write(hechos.tail())

# Dimensión del dataset
dim = st.radio("Dimensión a mostrar:", ("Filas", "Columnas"))
if dim == "Filas":
    st.write("Cantidad de filas:", hechos.shape[0])
else:
    st.write("Cantidad de columnas:", hechos.shape[1])

hechos['FECHA'] = pd.to_datetime(hechos['FECHA'])
hechos['Dia'] = hechos['FECHA'].dt.day
hechos['Mes'] = hechos['FECHA'].dt.month
hechos['Año'] = hechos['FECHA'].dt.year

st.subheader("Cantidad de víctimas por día y por año")

# Widget de selección para el año
años_únicos = hechos['Año'].unique()
año_seleccionado = st.selectbox("Selecciona un año:", años_únicos)

# Filtrar los datos por el año seleccionado
datos_año_seleccionado = hechos[hechos['Año'] == año_seleccionado]

# Visualización de víctimas por día en el año seleccionado
st.set_option('deprecation.showPyplotGlobalUse', False)  # Desactivar advertencia
plt.figure(figsize=(10, 6))
datos_por_dia = datos_año_seleccionado.groupby('Dia')['N_VICTIMAS'].sum()

# Crear el gráfico de barras con paleta de colores azul
sns.barplot(x=datos_por_dia.index, y=datos_por_dia.values, palette=sns.color_palette(["#2171b5"]))
plt.title(f'Distribución de víctimas por día en el año {año_seleccionado}')
plt.xlabel('Día del mes')
plt.ylabel('Cantidad de víctimas')
plt.xticks(np.arange(1, 32))  # Mostrar todos los días en el eje x
st.pyplot(plt)

# ... (resto del código)

# Visualización de víctimas por mes en el año seleccionado
plt.figure(figsize=(10, 6))
datos_por_mes = datos_año_seleccionado.groupby('Mes')['N_VICTIMAS'].sum()

# Crear el gráfico de barras con paleta de colores naranja
sns.barplot(x=datos_por_mes.index, y=datos_por_mes.values, palette=sns.color_palette(["#fc8d59"]))
plt.title(f'Distribución de víctimas por mes en el año {año_seleccionado}')
plt.xlabel('Mes')
plt.ylabel('Cantidad de víctimas')
plt.xticks(np.arange(1, 13))  # Mostrar todos los meses en el eje x
st.pyplot(plt)

# ... (resto del código)
