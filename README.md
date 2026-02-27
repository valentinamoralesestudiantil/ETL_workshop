# ETL_workshop
This repository contains the workshop development by Valentina Morales.
# Desarrollo de caso

A company has a CSV file with 50,000 rows of candidate request data from technical selection processes where each row represents a candidate request. With this, we want to be able to generate analytical queries and key performance indicators so that they are easy to interpret.

The first step that was taken into account is the realization of the requirements where it was understood that the company needed to respond with this from that the respective KPIs that were related to the requirements were made. Through the use of the grain, it was determined which dimensions were needed and what was going to be the level of complexity of each of them, dividing an attribute such as the Application Date into 3 new attributes (Day, month and year), in addition to adding other attributes that were considered important to answer the KPIs. Among other things, each of the attributes was divided by the dimensions we had decided.

## Grain table

<table>
  <tr>
    <th style="background-color: #00FFFF">First Name</th>
    <th style="background-color: #00FFFF">Last Name</th>
    <th style="background-color: #00FFFF">Email</th>
    <th style="background-color: #FF6347">Application Date = Day, month, year</th>
    <th style="background-color: #00FFFF">Country</th>
  </tr>
  <tr>
    <td style="background-color: #00FFFF">YOE</td>
    <td style="background-color: #90EE90">Seniority</td>
    <td style="background-color: #FFFF00">Technology</td>
    <td style="background-color: #FF6347">Approved by the Code Challenge</td>
    <td style="background-color: #FF6347">Approved by the Technical Interview</td>
  </tr>
  <tr>
    <td style="background-color: #FF6347">Approved in both tests</td>
    <td style="background-color: #FF6347">Code Challenge Score</td>
    <td style="background-color: #FF6347">Technical Interview Score</td>
  </tr>
</table>


## Table related to KPIs

It was decided to create a table of facts called **Application** this will contain 5 attributes of which 3 of them will be created by me because they are not in the original database, this to supply the need to have specific data that in this case will be BOOLEAN to more easily answer the doubts that are presented in the KPIs where it is asked to recognize which are the candidates who were hired in addition to information related to their scores in the tests, following the approval standards of the company, the rest of these attributes will represent the scores obtained in the tests by the candidates.

It also considered the dimension with which it was going to be related, the type of visualization and the justification of its commercial value for each of the KPIs to have a clearer knowledge of what was needed.
| Requerimientos | KPIs | Dimensiones | Tipo de visualización | Justificación de su valor comercial |
|----------------|------|-------------|-----------------------|------------------------------------|
| Cuantas contrataciones hay por cada una de las tecnologías | Hires by Technology | Technology | Gráfico de barras | Permite ver a la empresa cuales son las tecnologías más demandadas por la empresa y las que mas tienen índice de contratación y cuales no |
| Cuantas contrataciones hay por cada año | Hires by Year | Date | Gráfico de líneas | Permite ver a la empresa en que años se realizaron mas contrataciones y en cuales no para evaluar como va el crecimiento ademas de planificar un presupuesto |
| Cuantas contrataciones hay según el nivel de Seniority | Hires by Seniority | Seniority | Gráfico de barras | Permite ver a la empresa que seniority de las tecnologías es el mas contratado y cual no para así controlar los salarios y medir si se esta invirtiendo mas en talento experimentado o formación interna en la empresa |
| Cuantas contrataciones hay por cada país | Hires by Country over Years (Focus on USA, Brazil, Colombia, Ecuador) | Country | Gráfico de líneas múltiple | Permite ver a la empresa cuales son los países de donde mas personal fue contratado, esto permite analizar la expansión internacional y ver donde se debe priorizar el mercado |
| Cual es el puntaje promedio obtenido por los candidatos en el Code Challenge | Average score of the Code Challenge | Candidate | KPI Card | Permite ver a la empresa cuales son los puntajes en promedio que obtienen los candidatos que se postulan, esto sirve para evaluar como esta siendo el desempeño en las pruebas y si los resultados obtenidos es mas alto o bajo de lo esperado así se identifican brechas de habilidades y la efectividad del proceso de selección |
| Cual es el porcentaje de contratación en los años registrados | Hiring percentage | Candidate | Gráfico de torta | Permite ver a la empresa cuántos de los candidatos registrados han sido contratados para pasar las pruebas esto es representativo porque estiman como esta siendo la calidad de los postulantes para pasar los requerimientos propuestos y ayuda a optimizar costos de selección |
| Cual es el promedio de años de experiencia de las personas que fueron contratadas | Average years of experience | Candidate | KPI Card | Permite estimar a la empresa cuales son los años de experiencia de las personas que están contratando para así evaluar el nivel general de experiencia de las personas contratadas, ayudar a equilibrar los equipos de trabajo y ayudar en decisiones salariales |
