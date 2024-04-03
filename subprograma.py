def eliminar_elementos_repetidos(postres, ingredientes):
    postres_sin_repetidos = []
    ingredientes_sin_repetidos = []

    for i, postre in enumerate(postres):
        if postre not in postres_sin_repetidos:
            postres_sin_repetidos.append(postre)
            ingredientes_sin_repetidos.append(ingredientes[i])

    return postres_sin_repetidos, ingredientes_sin_repetidos

postres = ["Tarta de manzana", "Pastel de chocolate", "Helado de vainilla", "Tarta de manzana"]
ingredientes = [
    ["manzanas", "harina", "azúcar", "canela"],
    ["chocolate", "harina", "azúcar", "huevos"],
    ["crema de leche", "yemas de huevo", "azúcar", "vainilla"],
    ["manzanas", "harina", "azúcar", "canela"]
]

postres_sin_repetidos, ingredientes_sin_repetidos = eliminar_elementos_repetidos(postres, ingredientes)

print("Postres sin elementos repetidos:", postres_sin_repetidos)
print("Ingredientes correspondientes:", ingredientes_sin_repetidos)
