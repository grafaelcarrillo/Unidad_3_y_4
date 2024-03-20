import queue
import pandas as pd

def llenar_cola():
    cola = queue.Queue()
    i = 1
    datos = []
    while i <= 3:
        dato = input(f"Ingresa el dato {i}: ")
        if i > 3:
            break
        cola.put(int(dato))
        datos.append(int(dato))
        i += 1
    return cola, datos

def sumar_colas(cola1, cola2):
    suma_cola = queue.Queue()
    resultados = []
    while not cola1.empty() and not cola2.empty():
        suma_elementos = cola1.get() + cola2.get()
        suma_cola.put(suma_elementos)
        resultados.append(suma_elementos)
    return suma_cola, resultados

print("[Llenado de cola 1]")
cola1, datos_cola1 = llenar_cola()

print("\n[Llenado de cola 2]")
cola2, datos_cola2 = llenar_cola()

resultado, suma_resultados = sumar_colas(cola1, cola2)

df = pd.DataFrame({
    'Cola 1': datos_cola1,
    'Cola 2': datos_cola2,
    'Resultado': suma_resultados
})

print("Datos ingresados y resultados:")
print(df)
