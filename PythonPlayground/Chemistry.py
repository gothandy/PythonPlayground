recipes = {
    'plank': ['wood', 'knife'],
    'knife': ['iron', 'fire'],
    'fire': ['wood', 'flint'],
    }

materials = {
    'wood': 0,
    'blade': 0,
    'plank': 0,
    'fire': 0,
    'iron': 0,
    'flint': 0
    }


action = input(": ").split()

for product in iter(recipes):

    count = 0

    for ingredient in recipes[product]:

        if ingredient in action:
            count += 1

    if count == len(action):
        print(product)

        

