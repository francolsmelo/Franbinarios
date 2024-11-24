import mysql.connector

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="binarioshexa",  # Cambia esto al usuario de tu base de datos
            password="dualipa",   # Cambia esto a la contraseña de tu base de datos
            database="binarioshexa"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

def guardar_datos(numero, resultado_binario, resultado_hexadecimal):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            # Asumiendo que tienes una tabla llamada 'conversiones' con las columnas adecuadas
            query = """
            INSERT INTO conversiones (numero, resultado_binario, resultado_hexadecimal)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query, (numero, resultado_binario, resultado_hexadecimal))
            connection.commit()
        except mysql.connector.Error as err:
            print(f"Error al guardar datos: {err}")
        finally:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    db_conn = get_db_connection()
    if db_conn:
        print("Conexión exitosa a la base de datos.")
        db_conn.close()