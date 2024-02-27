import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar el DataFrame desde un archivo CSV
#file_path = 'https://github.com/Karrion1987/DATAOPS_SINIESTROS_VIALES/blob/main/EDA%20%2B%20ETL/df_siniestros_final.csv'
#df_siniestros_final = pd.read_csv(file_path)

# Título
st.title("App Streamlit sobre Siniestros Viales")

# Markdown
st.markdown("""
    El objetivo principal de este proyecto es analizar y visualizar datos relacionados con siniestros viales en la Ciudad de Buenos Aires. 
    A través de este análisis, buscamos identificar patrones, tendencias y áreas de alto riesgo para contribuir a la toma de decisiones informadas 
    y a la implementación de medidas preventivas.
    \nPara entrar en contexto tenemos un dataset llamado hechos y otro victimas proporcionado por HENRY para elaborar el proyecto de Data Analytics y llegar a una conclusión para poder tomar decisiones basadas en los datos.
""")

# Título e introducción
st.title("Dashboard de Power BI")
st.markdown("*")

# Embed del dashboard de Power BI
st.components.v1.iframe("https://app.powerbi.com/view?r=eyJrIjoiY2QyZTFjZmMtMGZkZS00ZjYyLWFlYTMtM2UyNzkzYmM4OGVkIiwidCI6IjRhMmE4MWRjLTE0MWQtNDM3My05MDgzLWQxNDY4YmRjYjE3NSIsImMiOjR9", 
width=800, height=600)


st.title("Conclusión y Recomendaciones")

texto_conclusion = """
En resumen, nuestro análisis revela que la tasa de homicidios por accidentes de tránsito entre 2016 y 2021 cumplió el objetivo solo en 2019 y 2021 comparando con el semestre anterior en cada caso. Sin embargo, el 2019 fue atípico debido a la pandemia y el confinamiento, lo que redujo significativamente los siniestros viales. Se observó una disminución de la tasa de accidentes con motos solo en 2018 y 2021, sugiriendo que las estrategias de prevención implementadas en esos años podrían ser efectivas para reducir incidentes futuros.

Es importante destacar que la mayoría de los siniestros involucran a peatones y motoristas. Se enfoca en estrategias de prevención y concientización ciudadana para mejorar la seguridad vial. Además, se nota que los accidentes en comunas disminuyeron en 2018 y 2021, señalando la efectividad de las medidas tomadas en esos años.

Estos hallazgos resaltan la necesidad de implementar estrategias similares en los próximos años para lograr una gestión efectiva de los accidentes viales y crear conciencia ciudadana.
"""

st.write(texto_conclusion)