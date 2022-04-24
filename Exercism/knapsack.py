def maximun_value(maximo, items):
    lista_peso = []
    for y in items:
        lista_peso.append(y['weight'])

    return lista_peso




items = [
  { "weight": 5, "value": 10 },
  { "weight": 4, "value": 40 },
  { "weight": 6, "value": 30 },
  { "weight": 4, "value": 50 }
]


print(maximun_value(10, items))