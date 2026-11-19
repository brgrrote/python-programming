# Problem 2-1
# A variable assigned to a name of a favorite restaurant
favorite_restaurant = "Texas Roadhouse"

# Print the value of the variable
print (favorite_restaurant)

# Change the value of the variable to a favorite dish 
favorite_restaurant = "Steak"

# Print the new value of the variable
print (favorite_restaurant)

# Problem 2-2
# A variable storing the name of the last business purchased from 
business_name = "Trio"

# A variable storing the item purchased on last trip 
item_purchased = "Matcha Latte"

# Print out a statement using the two variables
print("The last time I went to " + business_name + ", I purchased a " + item_purchased + ".")

# Problem 2-3
# A variable storing the name of a favorite car
favorite_car = "Porsche GT3 RS"

# Print out using lower, upper, and title case 
print(favorite_car.lower())
print(favorite_car.upper())
print(favorite_car.title())

# Problem 2-4
# A variable of a favorite quote 
favorite_quote = "Never be afraid to trust an unknown future to a known God."

# Add \t\n to the beggining and end of the quote using concatenation
favorite_quote = "\t\n" + favorite_quote + "\t\n"

# Print the quote 
print(favorite_quote) 

# Apply lstrip() to the quote and print it again
favorite_quote = favorite_quote.lstrip()
print(favorite_quote)

# Apply strip() to the quote and print it again
favorite_quote = favorite_quote.strip()
print(favorite_quote)

# Problem 2-5
# Create a math problem and store the result in a variable
result = 5*5+10/2

# Print the result with a message
print("The result of my math problem is: " + str(result))