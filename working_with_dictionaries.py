pizza_prefs = [{'name': 'sandeep', 'toppings': 'mushrooms', 'pizza type': 'round'},
               {'name': 'kylie', 'toppings': ['ham', 'pineapple'], 'pizza type': 'square'},
               {'name': 'lisa', 'toppings': ['mushrooms', 'peparroni'], 'pizza type': 'square'},
               {'name': 'dan', 'toppings': ['bacon', 'sausage', 'pepparoni'], 'pizza type': 'square'}]

for person in pizza_prefs:

    mushrooms_found = False

    if type(person['toppings']) is str:
      if(person['toppings']) == "mushrooms":
           mushrooms_found = True
    elif type(person['toppings']) is list:
        if("mushrooms" in person['toppings']):
            mushrooms_found = True

    if mushrooms_found: 
        print(person['name'] + " likes mushrooms")
                         