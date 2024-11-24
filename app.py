
from flask import Flask, render_template, request, redirect, url_for
from db_connection import get_db_connection
from guardar_datos import guardar_datos

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            numero = float(request.form['numero'])
            opcion = request.form['opcion'].strip().lower()

            if opcion == "binario":
                resultado_binario = bin(int(numero))[2:]
                resultado_hexadecimal = hex(int(numero))[2:]
                guardar_datos(numero, resultado_binario, resultado_hexadecimal)
            elif opcion == "hexadecimal":
                resultado_binario = bin(int(numero))[2:]
                resultado_hexadecimal = hex(int(numero))[2:]
                guardar_datos(numero, resultado_binario, resultado_hexadecimal)
            else:
                return render_template('index.html', error="Opción no válida. Por favor, elige 'binario' o 'hexadecimal'.")
                
            return render_template('index.html', resultado_binario=resultado_binario, resultado_hexadecimal=resultado_hexadecimal)
        except ValueError:
            return render_template('index.html', error="Por favor, ingresa un número válido.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)