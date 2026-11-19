pizza_prefs = [{'name': 'sandeep', 'toppings': 'mushrooms', 'pizza type': 'round'},
               {'name': 'kylie', 'toppings': ['ham', 'pineapple'], 'pizza type': 'square'},
               {'name': 'lisa', 'toppings': ['mushrooms', 'peparroni'], 'pizza type': 'square'},
               {'name': 'dan', 'toppings': ['bacon', 'sausage', 'pepparoni'], 'pizza type': 'square'}]

for person in pizza_prefs:
    if person['name'] == "sandeep":
        print(person['toppings'])
    else:
        print("This is not sandeep")
