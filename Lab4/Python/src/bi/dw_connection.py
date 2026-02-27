# src/bi/dw_connection.py

import mysql.connector
#Función para conectar con la base de datos MySQL, Cambia los parámetros según tu configuración de MySQL.
def get_connection():

    try:
        connection = mysql.connector.connect(
            host="localhost",        
            user="root",             
            password="valemoravale", 
            database="recruitment_dw" 
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")
        return None