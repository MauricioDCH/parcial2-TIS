from flask import Flask
import math

app = Flask(__name__)

@app.route('/factorial/<int:numero>')
def calcular_factorial(numero):
    factorial = math.factorial(numero)
    return f'El factorial de {numero} es: {factorial}' 

if __name__ == '__main__':
    app.run(debug=True)
