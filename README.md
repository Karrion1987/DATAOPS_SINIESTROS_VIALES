# DATAOPS SINIESTROS VIALES

![!\[alt text\](<Banner Fenix Ofertas y Descuentos Moderno Azul.png>)](<images/Banner Fenix Ofertas y Descuentos Moderno Azul.png>)

# Proyecto de Análisis de Siniestros Viales en la Ciudad Autónoma de Buenos Aires

## Presentación Personal

¡Hola! Mi nombre es [Allan] y estoy emocionado de presentar mi proyecto de análisis de siniestros viales en la Ciudad Autónoma de Buenos Aires. Soy [tu profesión o rol], apasionado por [temas relacionados con tu proyecto], y he decidido enfocar mis habilidades en mejorar la seguridad vial en nuestra ciudad.


## Objetivo del Proyecto

El objetivo principal de este proyecto es analizar y visualizar datos relacionados con siniestros viales en la Ciudad de Buenos Aires. A través de este análisis, buscamos identificar patrones, tendencias y áreas de alto riesgo para contribuir a la toma de decisiones informadas y a la implementación de medidas preventivas.

Este proyecto se realizó simulando ser un Data Analist de una consultora; y tiene como finalidad la elaboración de un análisis de datos solicitado por el Observatorio de Movilidad y Seguridad Vial (OMSV), bajo la órbita de la Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires (CABA).


## Descripción del Problema

En el contexto de una ciudad con altas densidades de tráfico y población como Buenos Aires, los siniestros viales representan una preocupación constante. Este proyecto tiene como objetivo principal analizar los datos de homicidios en siniestros viales entre los años 2016 y 2021 para proporcionar información crucial que guíe medidas de prevención efectivas.

## Estructura del Repositorio

*Notebooks:* Contiene el análisis exploratorio de datos (EDA) detallado y documentado. El notebook se centra en la búsqueda de valores faltantes, identificación de outliers y registros duplicados, y presenta gráficos significativos para entender las tendencias.

![!\[alt text\](image-2.png)](images/image-2.png)

*Dashboard:* Aquí encontrarás el  dashboard interactivo. Este dashboard proporciona una visión clara y detallada de las tendencias y patrones descubiertos durante el análisis.

![alt text](images/dashboard.png)

*Data:* Incluye el conjunto de datos utilizado para el análisis, denominado "hechos.xlsx", y "victimas.xlsx". Además, se detallan en el README del dataset las notas importantes para su uso el cual se fusiona para crear el archivo "df_siniestros_final.csv", listo para continuar con las demas etapas.

Las tasas de mortalidad relacionadas con siniestros viales suelen ser un indicador crítico de la seguridad vial en una región. Estas tasas se calculan, generalmente, como el número de muertes por cada cierto número de habitantes o por cada cierta cantidad de vehículos registrados. Reducir estas tasas es un objetivo clave para mejorar la seguridad vial y proteger la vida de las personas en la ciudad.

Para cumplir con ello, los datos iniciales que se utilizan son derivados de un dataset con información sobre homicidios de siniestros viales en la Ciudad de Buenos Aires, durante los años 2016-2021, que es de píblico acceso en la página oficial de CABA. 
Podemos acceder a ellos desde [Datos oficiales](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales)


*SQL:* En esta carpeta encontrarás scripts SQL utilizado para crear bases de datos relacionales que pueden ser utilizadas como fuente de datos para herramientas de visualización como Power BI y ademas como fuente remota de los datos.

![!\[alt text\](image-3.png)](images/image-3.png)

*Clever Cloud:* En este link encontrarás las conexiones de la base de datos MySQL utilizados para crear bases de datos en la nube  que pueden ser utilizadas como fuente de datos para herramientas de visualización como Power BI. [Clever Cloud](https://console.clever-cloud.com/) 

![!\[alt text\](image-4.png)](images/image-4.png)

*Material_Apoyo:* Recursos adicionales, como lecturas recomendadas, información del Observatorio de Movilidad y Seguridad Vial, y materiales que respaldan nuestro enfoque y decisiones durante el proyecto. [Población por Año](https://www.estadisticaciudad.gob.ar/eyc/wp-content/uploads/2040/05/CABA1040.xls)


## Dashboard Interactivo

Visita nuestro [Dashboard Interactivo](https://dataops-siniestros-labs.streamlit.app/) para explorar detalladamente los datos. Los filtros te permitirán navegar por la información de manera intuitiva, y la presentación visual facilitará la interpretación de los hallazgos.

## KPIs y Compromisos

En la sección de KPIs, encontrarás gráficos y métricas que miden nuestro progreso hacia dos objetivos clave: reducir en un 10% la tasa de homicidios en siniestros viales y en un 7% la cantidad de accidentes mortales de motociclistas y la cantidad de victimas en comunas con una reduccion del 5%.

![!\[alt text\](image.png)](images/image.png)

### Otras Métricas a considerar:
Tasa de accidentes por sexo masculino y femenino comparando con la tasa total.

![!\[alt text\](image-1.png)](images/image-1.png)

El [Repositorio](https://github.com/Karrion1987/DATAOPS_SINIESTROS_VIALES)
 en GitHub está organizado de la siguiente manera:

- **Notebooks:** Contiene los Jupyter Notebooks utilizados para la exploración y análisis de datos.
DATABASE SQL: [MYSQL](<DATABASE SQL/MYSQL SINIESTROS.sql>)	Contiene la base de datos SQL utilizada en el proyecto.
DATASET excel: [DATASET](<DATASET excel/homicidios.xlsx>)	Contiene el conjunto de datos en formato Excel.
EDA + ETL: [EDA](<EDA + ETL/EDA.ipynb>)	Contiene los scripts para el análisis exploratorio de datos (EDA) y la transformación, extracción y carga (ETL) de datos.
Streamlit: [APP](Streamlit/Inicio.py)	Contiene la aplicación web desarrollada con Streamlit.
images: [IMAGENES](images)	Contiene las imágenes utilizadas en el proyecto.
README.md: [README](README.md)	Contiene el archivo README con la descripción del proyecto.
SINIESTROS_VIALES.pbix: [DASHBOARD](SINIESTROS_VIALES.pbix)	Contiene el archivo Power BI con el análisis de los siniestros viales.
requirements.txt: [LIBRERIAS](requirements.txt)	Contiene los requisitos del proyecto.

## Conclusión y Recomendaciones

Lee nuestro reporte de análisis para obtener una visión detallada de nuestras conclusiones y recomendaciones. Este documento proporciona una síntesis de las acciones sugeridas para mejorar la seguridad vial en Buenos Aires.

## Contribuciones y Colaboraciones

Estoy abierto a contribuciones y colaboraciones de la comunidad. Si tienes ideas, sugerencias o te gustaría colaborar, no dudes en abrir un problema, realizar un pull request o ponerte en contacto conmigo.

## Agradecimientos

Agradezco a [Henry] por proporcionar datos valiosos para este proyecto.
Este proyecto no solo es un análisis de datos; es un esfuerzo colaborativo para hacer que las calles de Buenos Aires sean más seguras. ¡Gracias por explorar nuestro trabajo! 🚀💛
Gracias por tu interés y apoyo.

### Lenguajes de Programación
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Bibliotecas y Frameworks
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)

### Herramientas de Visualización
![Matplotlib](https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-013243?style=for-the-badge&logo=seaborn&logoColor=white)

### Bases de Datos
![SQL](https://img.shields.io/badge/SQL-003366?style=for-the-badge&logo=postgresql&logoColor=white)

### Herramientas de BI y Visualización
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=white)

### Procesamiento de Datos
![Excel](https://img.shields.io/badge/Microsoft%20Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

[¡Allan!]
