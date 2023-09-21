import numpy as np

def ingresarDatos(n):
    matriz = np.zeros((n, n), dtype=int)
    print("Ingresa los elementos de la matriz:")
    for i in range(n):
        for j in range(n):
            matriz[i][j] = int(input(f"Ingresa el elemento en la fila {i + 1}, columna {j + 1}: "))
    return matriz

def generarDatosAleatorios(n):
    matriz = np.random.choice([1, 0], size=(n, n))
    matriz = np.array([[0,0,0,1,1,0],[0,0,0,0,0,0],[0,0,0,0,0,1],[1,1,1,0,0,0],[0,1,1,0,0,1],[0,0,0,0,1,0]])   
    print(matriz)
    return matriz

def agregarUnosDiagonal(matriz):
    np.fill_diagonal(matriz, 1)
    print(matriz)
    return matriz

def calcularMatrizCaminos(matriz):
    n = len(matriz)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matriz[i][k] == 1 and matriz[k][j] == 1:
                    matriz[i][j] = 1
    print(matriz)
    return matriz

def ordenarFilasColumnas(matriz):
    filas_suma = []  
    for i in range(len(matriz)):
        suma = sum(matriz[i])
        filas_suma.append(suma)

    filas_ordenadas = sorted(range(len(matriz)), key=lambda x: filas_suma[x], reverse=True)

    matriz_ordenada = []
    for i in filas_ordenadas:
        fila_ordenada = [matriz[i][j] for j in filas_ordenadas]
        matriz_ordenada.append(fila_ordenada)
    matriz_ordenada_np = np.array(matriz_ordenada)    
    print(matriz_ordenada_np)    
    return matriz_ordenada_np

while True:
    print("\nMenú:")
    print("1. Generar una matriz aleatoriaa")
    print("2. Ingresar datos manualmente")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1" or opcion == "2":
        n = int(input("\nIngresa el número de filas y columnas de la matriz (entre 5 y 15): "))
        if 5 <= n <= 15:
            if opcion == "1":
                matriz = generarDatosAleatorios(n)
            else:
                matriz = ingresarDatos(n)
            
            print("\nAgregando unos a la diagonal...\n")
            agregarUnosDiagonal(matriz)
            print("\nHallando la matriz de caminos...\n")
            calcularMatrizCaminos(matriz)
            print("\nOrdenando las filas y columnas\n")
            ordenarFilasColumnas(matriz)
        else:
            print('El valor debe estar entre 5 y 15')
    
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")