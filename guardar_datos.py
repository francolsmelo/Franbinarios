# guardar_datos.py

from db_connection import get_db_connection

def guardar_datos(numero, binario, hexadecimal):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        insert_query = "INSERT INTO conversiones (entero, binario, hexadecimal) VALUES (%s, %s, %s)"
        data = (numero, binario, hexadecimal)
        cursor.execute(insert_query, data)

        connection.commit()
        ##print("Datos guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar datos: {e}")
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    # No necesitamos datos de ejemplo aquí, ya que los recibimos desde binarioshexa.py
    pass