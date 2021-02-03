import json


def IngresarCarton(carton):
    with open('Cartones.json', 'w') as C:
        json.dump(carton, C, indent=4, sort_keys=True)

