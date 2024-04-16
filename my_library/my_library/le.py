class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.next = None 

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def Vacia (self):
        return self.primero == None
    
    def Agregar_Ultimo (self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux=self.ultimo
            self.ultimo = aux.next = Nodo(dato)

    def Imprimir_Lista (self):
        node = self.primero
        while node != None:
            print(node.dato, end =" => ")
            node = node.next
    
    def Eliminar_Ultimo (self):
        aux=self.primero
        while aux.next != self.ultimo:
            aux= aux.next
        aux.next= None
        self.ultimo=aux

    def Agregar_Inicio (self, dato):
        if self.Vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.next = self.primero
            self.primero = aux

    def Eliminar_Inicio(self):
        self.primero = self.primero.next

    
