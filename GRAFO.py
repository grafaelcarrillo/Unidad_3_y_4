import networkx as nx

GRAFO = nx.Graph()

estados = ["Aguascalientes", "Baja California", "Chiapas", "Durango", "Estado de México", "Guerrero", "Hidalgo"]

relaciones = [("Aguascalientes", "Baja California", {"costo": 10}),
              ("Aguascalientes", "Chiapas", {"costo": 20}),
              ("Aguascalientes", "Durango", {"costo": 15}),
              ("Baja California", "Chiapas", {"costo": 25}),
              ("Baja California", "Durango", {"costo": 30}),
              ("Baja California", "Estado de México", {"costo": 35}),
              ("Chiapas", "Guerrero", {"costo": 40}),
              ("Durango", "Estado de México", {"costo": 45}),
              ("Estado de México", "Hidalgo", {"costo": 50}),
              ("Guerrero", "Hidalgo", {"costo": 55})]

GRAFO.add_nodes_from(estados)
GRAFO.add_edges_from(relaciones)

print("Diccionario de conexiones:")
print(GRAFO.adj)

def calcular_costo_total(recorrido):
    costo_total = 0
    for i in range(len(recorrido) - 1):
        costo_total += GRAFO[recorrido[i]][recorrido[i+1]]['costo']
    return costo_total

recorrido_a = nx.algorithms.hamiltonian_path(GRAFO)
print("Recorrido a):", list(recorrido_a))
print("Costo total a):", calcular_costo_total(list(recorrido_a)))

recorrido_b = nx.algorithms.eulerian_circuit(GRAFO)
print("Recorrido b):", list(recorrido_b))
print("Costo total b):", calcular_costo_total(list(recorrido_b)))
