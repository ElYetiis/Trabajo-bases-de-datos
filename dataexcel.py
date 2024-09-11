import pandas as pd 
from mysql.connector import Error
import mysql.connector

# Cargar el archivo Excel
df = pd.read_excel('data1.xlsx', sheet_name='Data')

# Seleccionar solo las columnas necesarias
df = df[['Employee_ID', 'Full_Name', 'Job_Title', 'Department', 'Business_Unit',
         'Gender', 'Ethnicity', 'Age', 'Annual_Salary', 'Bonus']]

# Convertir filas a lista de listas
filas = df.values.tolist()

# Imprimir para verificar el contenido de las filas
print("Contenido de las filas:")
for i, fila in enumerate(filas[:5]):
    print(f"Fila {i+1}: {fila}")

try:
    # Conexión a la base de datos
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='Ilov3yoursmile',
        database='carga_m_A'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        
        # Ejecutar inserción masiva
        sql = """
            INSERT INTO empleados(
                Employee_ID,
                Full_Name, 
                Job_Title,
                Department, 
                Business_Unit, 
                Gender, 
                Ethnicity,
                Age,
                Annual_Salary,
                Bonus
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.executemany(sql, filas)
        connection.commit()
        print(f"{cursor.rowcount} filas insertadas.")
        
except Error as ex:
    print(f"Error en la conexión: {ex}")

finally:
    if connection.is_connected():
        connection.close()
        print("Conexión cerrada.")
