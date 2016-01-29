recipes = {
    'plank': ['wood', 'blade'],
    'blade': ['iron', 'fire'],
    'fire': ['wood', 'flint'],
    }

materials = {
    'wood': 2,
    'blade': 0,
    'plank': 0,
    'fire': 0,
    'iron': 1,
    'flint': 1
    }

def checkIngredients(product):

    for ingredient in recipes[product]:
        if materials[ingredient] < 1:
            print("You need {0}".format(ingredient))
            return False

    return True

def makeProduct(product):

    for ingredient in recipes[product]:
        materials[ingredient] += -1

    materials[product] += 1

    return True

def cook(action):

    for product in iter(recipes):

        count = 0

        for ingredient in recipes[product]:

            if ingredient in action:
                count += 1

        if count == len(action):

            if checkIngredients(product):

                makeProduct(product)

                print(product)

    return True

while cook(input(": ").split()):
    pass


