import pandas as pd
import pyodbc

# Establecer la conexión con la base de datos SQL Server
server = 'DESKTOP-5SRJD1M\SQLEXPRESS'
database = 'Taller2'
username = 'kcUser'
password = '13demayo'
try:
    # Leer el archivo CSV
    df = pd.read_csv('datos.csv')

    # Establecer la conexión con la base de datos
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
    cursor = conn.cursor()

    # Crear la tabla 'datos' si no existe
    cursor.execute('''
        IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'datos')
        CREATE TABLE datos (
            Campo1 NVARCHAR(255),
            Campo2 NVARCHAR(255),
            Campo3 NVARCHAR(255)
        )
    ''')
    conn.commit()

    # Insertar los datos del CSV en la tabla 'datos'
    for index, row in df.iterrows():
        cursor.execute('''
            INSERT INTO datos (Campo1, Campo2, Campo3)
            VALUES (?, ?, ?)
        ''', (str(row['Campo1']), str(row['Campo2']), str(row['Campo3'])))

    conn.commit()

    # Mostrar todos los registros de la tabla 'datos'
    cursor.execute("SELECT Campo1, Campo2, Campo3 FROM datos")
    rows = cursor.fetchall()

    if rows:
        print("Registros encontrados en la tabla 'datos':")
        for row in rows:
            campo1, campo2, campo3 = row
            print(f"Campo1: {campo1}, Campo2: {campo2}, Campo3: {campo3}")
    else:
        print("No se encontraron registros en la tabla 'datos'.")

    # Cerrar la conexión
    conn.close()

except Exception as e:
    print("Error al conectar a la base de datos o al procesar los datos:", e)
