import mysql.connector

# Configuración de la conexión
config = {
    'host': 'bcj9asygzv10rjmwhyss-mysql.services.clever-cloud.com',
    'user': 'u3qdp6wlms7b0pdx',
    'password': '2xtwfSLG924Lt1Zt7P8v',
    'database': 'bcj9asygzv10rjmwhyss',
    'port': 3306
}

# Conexion a mysql 
connection = mysql.connector.connect(**config)

# Verificar la conexion 
try: 
    cursor = connection.cursor()
    cursor.execute("SELECT DATABASE();")
    db = cursor.fetchone()
    print(f"Conectado a la base de datos: {db[0]}")
    cursor.close()
except mysql.connector.Error as err:
        print(f"Error al conectar: {err}")
        


