import pandas as pd


# create dim time
def create_dim_date(df):
    # Hacer una copia del DataFrame original para no modificarlo
    df = df.copy()
    # Convierte la columna 'application_date' a formato datetime de Pandas esto para poder manipular facilmente la fecha
    df["application_date"] = pd.to_datetime(df["application_date"])
    # Crea una nueva columna 'date_key' con un formato de fecha YYYYMMDD (entero)
    df["date_key"] = df["application_date"].dt.strftime("%Y%m%d").astype(int)
    # Elimina duplicados y crea una copia del DataFrame con las columnas necesarias
    dim_date = df[["date_key", "application_date"]].drop_duplicates().copy()
    # Extrae año, mes y día de 'application_date'
    dim_date["year"] = dim_date["application_date"].dt.year
    dim_date["month"] = dim_date["application_date"].dt.month
    dim_date["day"] = dim_date["application_date"].dt.day
    # Reorganiza las columnas de la dimensión de tiempo
    dim_date = dim_date[["date_key", "day", "month", "year"]]

    return dim_date


#sirve para crear tablas de dimensiones para categorias especificas, normaliza los datos y evita redundacia
# Create dims seniority, country, technology
def create_dimension(df, column_name, key_name):
    # Hacer una copia del DataFrame original para no modificarlo
    df = df.copy()
    # Elimina los duplicados de la columna seleccionada y restablece los índices
    dim = df[[column_name]].drop_duplicates().reset_index(drop=True)
    # Crea una nueva columna con claves numéricas (index + 1)
    dim[key_name] = dim.index + 1
    # Selecciona solo las columnas necesarias y devuelve la dimensión
    dim = dim[[key_name, column_name]]

    return dim



# Dim candidate
def create_dim_candidate(df):

    dim_candidate = df[["first_name", "last_name", "email" , "yoe"]] \
        .drop_duplicates().reset_index(drop=True)

    dim_candidate["candidate_key"] = dim_candidate.index + 1

    dim_candidate = dim_candidate[
        ["candidate_key", "first_name", "last_name", "email" , "yoe"]
    ]

    return dim_candidate




# Fact table application 
def create_fact_table(df,
                      dim_country,
                      dim_seniority,
                      dim_technology,
                      dim_candidate
                      ):
    
    df["application_date"] = pd.to_datetime(df["application_date"])
    df["date_key"] = df["application_date"].dt.strftime("%Y%m%d").astype(int)

    # Unir los DataFrames de dimensiones a la tabla de hechos
    df = df.merge(dim_country, on="country", how="left")
    df = df.merge(dim_seniority, on="seniority", how="left")
    df = df.merge(dim_technology, on="technology", how="left")
    df = df.merge(dim_candidate,
                  on=["first_name", "last_name", "email", "yoe"],
                  how="left")
    
    
    # Asignar valores booleanos de acuerdo con las calificaciones
    df["approved_by_the_code_challenge"] = (df["code_challenge_score"] >= 7).astype(bool)
    df["approved_by_the_technical_interview"] = (df["technical_interview_score"] >= 7).astype(bool)
    # Crear una columna para la aprobación en ambos exámenes
    df["approved_in_both_tests"] = (
        (df["code_challenge_score"] >= 7) &
        (df["technical_interview_score"] >= 7)
    ).astype(bool)
    # Seleccionar las columnas de la tabla de hechos
    fact_application = df[[
        "code_challenge_score",
        "technical_interview_score",
        "approved_by_the_code_challenge",
        "approved_by_the_technical_interview",
        "approved_in_both_tests",
        "country_key",
        "candidate_key",
        "technology_key",
        "seniority_key",
        "date_key"
    ]].copy()

    return fact_application


# Transform complete
def transform_data(df):
#creacion de tablas de dimensiones
    dim_date = create_dim_date(df)
    dim_country = create_dimension(df, "country", "country_key")
    dim_seniority = create_dimension(df, "seniority", "seniority_key")
    dim_technology = create_dimension(df, "technology", "technology_key")
    dim_candidate = create_dim_candidate(df)

    fact_application = create_fact_table(
        df,
        dim_country,
        dim_seniority,
        dim_technology,
        dim_candidate,
    )

    return {
        "dim_date": dim_date,
        "dim_country": dim_country,
        "dim_seniority": dim_seniority,
        "dim_technology": dim_technology,
        "dim_candidate": dim_candidate,
        "fact_application": fact_application
    }