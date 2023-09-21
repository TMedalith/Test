from flask import Flask, render_template, request
import random
import numpy as np

app = Flask(__name__)

matriz_generada = np.array([])
matriz_unos_diagonal = np.array([])
matriz_caminos = np.array([])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procesar_matriz', methods=['POST'])
def procesar_matriz():
        global matriz_generada, matriz_unos_diagonal, matriz_caminos
        n = int(request.form['n'])

        matriz_generada = np.random.choice([1, 0], size=(n, n))
        
        matriz_unos_diagonal = matriz_generada.copy()
        np.fill_diagonal(matriz_unos_diagonal, 1)
        
        matriz_caminos = matriz_unos_diagonal.copy()
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matriz_caminos[i][k] == 1 and matriz_caminos[k][j] == 1:
                        matriz_caminos[i][j] = 1
       
        return render_template('index.html',
        matriz_generada=matriz_generada.tolist(),
        matriz_unos_diagonal=matriz_unos_diagonal.tolist(),
        matriz_caminos=matriz_caminos.tolist(),
        n=n)


if __name__ == '__main__':
    app.run(debug=True)
