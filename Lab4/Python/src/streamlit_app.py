# src/streamlit_app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bi.dw_connection import get_connection  # Importa la conexión

# Ejecutar consulta SQL y devolver un DataFrame
def run_query(query):
    conn = get_connection()  # Usa tu función de conexión
    if conn:
        df = pd.read_sql(query, conn)  # Realiza la consulta
        conn.close()  # Cierra la conexión después de obtener los datos
        return df
    else:
        st.error("No se pudo conectar a la base de datos.")
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error


# Consulta 1: Contrataciones por Tecnología
query_tech = """
SELECT t.technology, COUNT(f.application_key) AS hires
FROM fact_application f
JOIN dim_technology t ON f.technology_key = t.technology_key
WHERE f.approved_in_both_tests = 1
GROUP BY t.technology
"""
df_tech = run_query(query_tech)

# Gráfico de barras para Contrataciones por Tecnología
st.subheader("Hires by Technology")
fig_tech, ax_tech = plt.subplots(figsize=(14, 8))
sns.barplot(x="hires", y="technology", data=df_tech, ax=ax_tech)
ax_tech.set_title("Hires by Technology")
# Añadir etiquetas con los valores de las barras
ax_tech.bar_label(ax_tech.containers[0], fmt='%d', padding=5) 
plt.tight_layout()  # Ajustar para que las etiquetas no se superpongan
# Guardar el gráfico en la carpeta 'output'
fig_tech.savefig('output/Hires by Technology.png')
# Guardar los datos en un archivo CSV
df_tech.to_csv('output/hires_by_technology.csv', index=False)
st.pyplot(fig_tech)

# Consulta 2: Contrataciones por Año
query_year = """
SELECT d.year, COUNT(f.application_key) AS hires
FROM fact_application f
JOIN dim_date d ON f.date_key = d.date_key
WHERE f.approved_in_both_tests = 1
GROUP BY d.year
ORDER BY d.year
"""
df_year = run_query(query_year)

# Gráfico de líneas para Contrataciones por Año
st.subheader("Hires by Year")
fig_year, ax_year = plt.subplots()
sns.lineplot(x="year", y="hires", data=df_year, ax=ax_year, marker="o")
ax_year.set_title("Hires by Year")
ax_year.set_xticks(df_year['year'])  # Establecer los valores del eje X como los años
ax_year.set_xticklabels(df_year['year'].astype(int))  # Mostrar solo los años enteros
# Guardar el gráfico en la carpeta 'output'
fig_year.savefig('output/Hires by Year.png')
# Guardar los datos en un archivo CSV
df_year.to_csv('output/hires_by_year.csv', index=False)
st.pyplot(fig_year)

# Consulta 3: Contrataciones por Nivel de Seniority
query_seniority = """
SELECT s.seniority, COUNT(f.application_key) AS hires
FROM fact_application f
JOIN dim_seniority s ON f.seniority_key = s.seniority_key
WHERE f.approved_in_both_tests = 1
GROUP BY s.seniority
"""
df_seniority = run_query(query_seniority)

# Gráfico de barras para Contrataciones por Nivel de Seniority
st.subheader("Hires by Seniority")
fig_seniority, ax_seniority = plt.subplots()
sns.barplot(x="hires", y="seniority", data=df_seniority, ax=ax_seniority)
ax_seniority.set_title("Hires by Seniority")
# Ajustar el límite superior del eje X a 1200
ax_seniority.set_xlim(0, 1200)  # Cambia el límite superior del eje X
ax_seniority.bar_label(ax_seniority.containers[0], fmt='%d', padding=8, label_type='edge')
# Ajustar el espacio para que las etiquetas no se superpongan
plt.tight_layout()
# Guardar el gráfico en la carpeta 'output'
fig_seniority.savefig('output/Hires by Seniority.png')
# Guardar los datos en un archivo CSV
df_seniority.to_csv('output/hires_by_seniority.csv', index=False)
st.pyplot(fig_seniority)



# Consulta 4: Contrataciones por País (Estados Unidos, Brasil, Colombia, Ecuador)
query_country = """
SELECT c.country, COUNT(f.application_key) AS hires
FROM fact_application f
JOIN dim_country c ON f.country_key = c.country_key
WHERE f.approved_in_both_tests = 1
  AND c.country IN ('United States of America', 'Brazil', 'Colombia', 'Ecuador')
GROUP BY c.country
"""
df_country = run_query(query_country)

# Gráfico de líneas para Contrataciones por País
st.subheader("Hires by Country over Years (Focus on USA, Brazil, Colombia, Ecuador)")
fig_country, ax_country = plt.subplots()
sns.lineplot(x="country", y="hires", data=df_country, ax=ax_country, marker="o")
ax_country.set_title("Hires by Country")
# Guardar el gráfico en la carpeta 'output'
fig_country.savefig('output/Hires by Country over Years.png')
# Guardar los datos en un archivo CSV
df_country.to_csv('output/hires_by_country.csv', index=False)
st.pyplot(fig_country)

# Consulta 5: Puntaje Promedio del Code Challenge
query_avg_score = """
SELECT AVG(f.code_challenge_score) AS avg_score
FROM fact_application f
WHERE f.approved_in_both_tests = 1
"""
df_avg_score = run_query(query_avg_score)
avg_score = df_avg_score['avg_score'][0]

# Mostrar Puntaje Promedio en KPI Card
st.subheader("Average score of the Code Challenge")
# Añadir estilo CSS para el recuadro
st.markdown(f"""
    <style>
        .kpi-card {{
            background-color: #1e1e1e;
            color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            font-size: 32px;
            text-align: center;
        }}
        .kpi-card .label {{
            font-size: 20px;
            font-weight: bold;
        }}
        .kpi-card .value {{
            font-size: 48px;
            font-weight: 600;
            margin-top: 10px;
        }}
    </style>
    <div class="kpi-card">
        <div class="label">Average score of the Code Challenge</div>
        <div class="value">{avg_score:.2f} </div>
    </div>
""", unsafe_allow_html=True)

# Guardar en el archivo CSV en la carpeta 'output/'
df_avg_score.to_csv('output/avg_code_challenge_score.csv', index=False)

# Consulta 6: Porcentaje de Contratación por Año
query_hiring_percentage = """
SELECT d.year, 
       (COUNT(f.application_key) / (SELECT COUNT(*) FROM fact_application WHERE approved_in_both_tests = 1)) * 100 AS hiring_percentage
FROM fact_application f
JOIN dim_date d ON f.date_key = d.date_key
WHERE f.approved_in_both_tests = 1
GROUP BY d.year
"""
df_hiring_percentage = run_query(query_hiring_percentage)

# Gráfico de torta para Porcentaje de Contratación por Año
st.subheader("Hiring percentage")
fig_hiring, ax_hiring = plt.subplots()
ax_hiring.pie(df_hiring_percentage['hiring_percentage'], labels=df_hiring_percentage['year'], autopct='%1.1f%%')
ax_hiring.set_title("Hires Percentage by Year")
# Guardar el gráfico en la carpeta 'output'
fig_hiring.savefig('output/Hiring percentage.png')
# Guardar los datos en un archivo CSV
df_hiring_percentage.to_csv('output/hiring_percentage.csv', index=False)
st.pyplot(fig_hiring)

# Consulta 7: Promedio de Años de Experiencia de los Contratados
query_avg_experience = """
SELECT AVG(c.yoe) AS avg_experience
FROM fact_application f
JOIN dim_candidate c ON f.candidate_key = c.candidate_key
WHERE f.approved_in_both_tests = 1
"""
df_avg_experience = run_query(query_avg_experience)
avg_experience = df_avg_experience['avg_experience'][0]

# Mostrar Promedio de Años de Experiencia en KPI Card
st.subheader("Average years of experience")
# Añadir estilo CSS para el recuadro
st.markdown(f"""
    <style>
        .kpi-card {{
            background-color: #1e1e1e;
            color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            font-size: 32px;
            text-align: center;
        }}
        .kpi-card .label {{
            font-size: 20px;
            font-weight: bold;
        }}
        .kpi-card .value {{
            font-size: 48px;
            font-weight: 600;
            margin-top: 10px;
        }}
    </style>
    <div class="kpi-card">
        <div class="label">Average Experience</div>
        <div class="value">{avg_experience:.2f} years</div>
    </div>
""", unsafe_allow_html=True)
# Guardar en el archivo CSV en la carpeta 'output/'
df_avg_experience.to_csv('output/avg_years_of_experience.csv', index=False)


