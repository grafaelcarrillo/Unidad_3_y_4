from queue import Queue

class SistemaColasSeguros:
    def __init__(self):
        self.colas_servicios = {}

    def agregar_cola_servicio(self, nombre):
        self.colas_servicios[nombre] = Queue()

    def llegada_cliente(self, servicio, numero_cliente):
        if servicio in self.colas_servicios:
            self.colas_servicios[servicio].put(numero_cliente)

    def atender_cliente(self, servicio):
        if servicio in self.colas_servicios:
            cola_servicio = self.colas_servicios[servicio]
            if not cola_servicio.empty():
                return cola_servicio.get()
            else:
                return "No hay clientes en la cola de servicio " + servicio
        else:
            return "El servicio " + servicio + " no existe"

sistema_colas_seguros = SistemaColasSeguros()
sistema_colas_seguros.agregar_cola_servicio("auto")
sistema_colas_seguros.agregar_cola_servicio("hogar")
sistema_colas_seguros.agregar_cola_servicio("vida")

sistema_colas_seguros.llegada_cliente("auto", 1)
sistema_colas_seguros.llegada_cliente("hogar", 2)
sistema_colas_seguros.llegada_cliente("vida", 3)

print("Se ha llegado un cliente para el servicio de auto, número de atención:", sistema_colas_seguros.atender_cliente("auto"))
print("Se ha llegado un cliente para el servicio de hogar, número de atención:", sistema_colas_seguros.atender_cliente("hogar"))

