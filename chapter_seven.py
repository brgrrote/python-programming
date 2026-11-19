# Probem 7-1:
# Ask a user for their favorite restaurant and print a message 
fav_restaurant = input("Input your favorite restaurant: ")

print("Let me help you find the closest " + fav_restaurant)

# Problem 7-2:
# Ask a user for two numbers and multiply it together
number1 = float(input("Choose a number: "))
number2 = float(input("Choose another number: "))

result = number1 * number2

# Print the result
print("Result: ", result)

# Problem 7-3:
# Create an empty list to store dinner items
dinner_list = []

# Start the while loop
while True:
    dinner = input("What are you having for dinner? ('D' if finish listing) :")

    # Check if the user wants to exit the loop 
    if dinner.upper() == 'D':
        break

    # Add the item to the list
    dinner_list.append(dinner)

# Print the final list of items
print("\nYour dinner menu is: ")
for food in dinner_list:
    print("-", food)

# Problem 7-4:
# Let the user choose from the three rides
rides = [{'Ride':'Ferris Wheel', 'Price':'$2'},
         {'Ride':'Tilt-A-Whirl', 'Price':'$3'},
         {'Ride':'Pirate Ship', 'Price':'$3.50'}]

program_running = True

while program_running:
    user_ride = input("Which ride would you like to go on? (Ferris Wheel, Tilt-A-Whirl, Pirate Ship)"
                      "Type 'exit' to quit: ")

    # Check if the user wants to quit:
    if user_ride.lower() == "exit":
        program_running = False

    # Check if the selected rides exists in the list
    elif user_ride == rides[0]['Ride']:
        print("Please pay " + rides[0]['Price'] + ".")
    elif user_ride == rides[1]['Ride']:
       print("Please pay " + rides[1]['Price'] + ".")
    elif user_ride == rides[2]['Ride']:
       print("Please pay " + rides[2]['Price'] + ".")
    else:
        print("Ride was not found.")

print("Thank you for visiting the carnival!")

# Problem 7-5:
# Create a list of grocery items and have one item appear multiple times.  
grocery_list = ['Meat', 'Egg', 'Toothbrush', 'Water', 'Water', 'Shirt', 'Water']

print("Original Grocery List:", grocery_list)

# Item that was not purchased from the list
item_remove = 'Water'

# Loop through the grocery list and remove the selected item
while item_remove in grocery_list:
    grocery_list.remove(item_remove)

print("\nUpdated Grocery List: ", grocery_list)






      