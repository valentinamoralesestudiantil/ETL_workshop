import pandas as pd
from tabulate import tabulate
from log import log_progress
from extract import extract_candidates
from transform import transform_data
from load import save_dimensions_to_csv, load_to_dw
import streamlit as st
from src.streamlit_app import app  # Importa tu código de visualización


def main():
    #almacena los logs
    log_file = r"/Users/valemoravale/Documents/UNIVERSIDAD /Semestre 5/ETL/Lab4/Python/logs/log_file.txt" 
    #almacena los archivos transformados
    target_file = r"/Users/valemoravale/Documents/UNIVERSIDAD /Semestre 5/ETL/Lab4/Python/data/transformed"
    data_path = r"/Users/valemoravale/Documents/UNIVERSIDAD /Semestre 5/ETL/Lab4/Python/data/raw/candidates.csv"


    # Log the initialization of the ETL process 
    log_progress('Starting ETL process', log_file)

    # Extract
    log_progress('Extract phase started', log_file)
    #llama a la funcion y extrae los datos
    df_candidates = extract_candidates(data_path)
    #Muestra las primeras filas de df_candidate en formato tabular
    print(tabulate(df_candidates.head(), headers='keys', tablefmt='psql'))
    log_progress("Extract phase complete", log_file)


    # Transform
    log_progress("Transform phase Started", log_file) 
    #llama a la funcion de transformar y transforma los dartos extraidos
    df_candidates_transform = transform_data(df_candidates)

    #Muestra algunos datos de las transformacion 
    print("\nDIM_DATE")
    print(tabulate(df_candidates_transform["dim_date"].head(), headers='keys', tablefmt='psql'))

    print("\nDIM_COUNTRY")
    print(tabulate(df_candidates_transform["dim_country"].head(), headers='keys', tablefmt='psql'))

    print("\nDIM_SENIORITY")
    print(tabulate(df_candidates_transform["dim_seniority"].head(), headers='keys', tablefmt='psql'))

    print("\nDIM_TECHNOLOGY")
    print(tabulate(df_candidates_transform["dim_technology"].head(), headers='keys', tablefmt='psql'))

    print("\nDIM_CANDIDATE")
    print(tabulate(df_candidates_transform["dim_candidate"].head(), headers='keys', tablefmt='psql'))

    print("\nFACT_APPLICATION")
    print(tabulate(df_candidates_transform["fact_application"].head(), headers='keys', tablefmt='psql'))

    log_progress('Transform phase complete', log_file)



    # Load
    log_progress('Load phase started', log_file)
    #Guarda las tablas de dimensiones y hechos en archivos CSV en el directorio target_file
    save_dimensions_to_csv(
        target_file,
        dim_date=df_candidates_transform["dim_date"],
        dim_country=df_candidates_transform["dim_country"],
        dim_seniority=df_candidates_transform["dim_seniority"],
        dim_technology=df_candidates_transform["dim_technology"],
        dim_candidate=df_candidates_transform["dim_candidate"],
        fact_application=df_candidates_transform["fact_application"]
    )
    #cargar las transformaciones a un data warehouse
    load_to_dw(df_candidates_transform)
    log_progress('Load phase complete', log_file)


    # ETL process
    log_progress('ETL process finished successfully', log_file)

#BI
    st.set_page_config(page_title="Dashboard", layout="wide")
    app.run()  # Llama a la función que ejecutará el código de Streamlit

if __name__ == "__main__":
    main()
