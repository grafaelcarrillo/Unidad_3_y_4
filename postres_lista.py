postres = ["Tarta de manzana", "Pastel de chocolate", "Helado de vainilla"]
ingredientes = [
    ["manzanas", "harina", "azúcar", "canela"],
    ["chocolate", "harina", "azúcar", "huevos"],
    ["crema de leche", "yemas de huevo", "azúcar", "vainilla"]
]

def imprimir_ingredientes(postre):
    if postre in postres:
        index = postres.index(postre)
        print("Ingredientes de", postre + ":")
        for ingrediente in ingredientes[index]:
            print("-", ingrediente)
    else:
        print("El postre", postre, "no existe.")

def insertar_ingredientes(postre, nuevos_ingredientes):
    if postre in postres:
        index = postres.index(postre)
        ingredientes[index].extend(nuevos_ingredientes)
        print("Se han añadido nuevos ingredientes al postre", postre + ".")
    else:
        print("El postre", postre, "no existe.")

def eliminar_ingredientes(postre, ingredientes_a_eliminar):
    if postre in postres:
        index = postres.index(postre)
        for ingrediente in ingredientes_a_eliminar:
            if ingrediente in ingredientes[index]:
                ingredientes[index].remove(ingrediente)
        print("Se han eliminado ingredientes del postre", postre + ".")
    else:
        print("El postre", postre, "no existe.")

def añadir_postre_nuevo(postre, lista_de_ingredientes):
    postres.append(postre)
    ingredientes.append(lista_de_ingredientes)
    print("Se ha dado de alta el postre", postre + " con sus ingredientes.")

def eliminar_postre_existente(postre):
    if postre in postres:
        index = postres.index(postre)
        del postres[index]
        del ingredientes[index]
        print("Se ha dado de baja el postre", postre + " y sus ingredientes.")
    else:
        print("El postre", postre, "no existe.")

imprimir_ingredientes("Tarta de manzana")
insertar_ingredientes("Tarta de manzana", ["limón", "mantequilla"])
imprimir_ingredientes("Tarta de manzana")
eliminar_ingredientes("Tarta de manzana", ["limón", "harina"])
imprimir_ingredientes("Tarta de manzana")
eliminar_postre_existente("Tarta de manzana")
imprimir_ingredientes("Tarta de manzana")
añadir_postre_nuevo("Flan", ["leche", "huevos","vainilla", "azúcar", "leche evaporada", "leche condensada"])
imprimir_ingredientes("Flan")