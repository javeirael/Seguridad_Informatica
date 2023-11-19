def tabla_de_multiplicar(numero, rango):
    for i in range(1, rango + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")