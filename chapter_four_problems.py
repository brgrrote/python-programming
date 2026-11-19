<<<<<<< HEAD
# Problem 4-1
# Store favorite places to visit in a list 
favorite_places = ["Beijing", "Tokyo", "Seoul", "Palawan"]

# Use a for loop to print each place in the list with added phrase
for place in favorite_places:
    print(place + " is a nice place to visit.")

# Problem 4-2
# Use a for loop to print the numbers from 90 to 100
for number in range(90,101):
    print(number)

# Problem 4-3
# Create a list of numbers from 100,000 to 1,000,000 
numbers = list(range(100000, 1000001))

# Calculate and print the sum of all numbers
print(sum(numbers))

# Problem 4-4
# Create a list of numbers placed randomly 
random_numbers = [5, 10, 6, 1, 9, 7, 2, 11, 3, 8, 4, 12, 15, 13, 19, 16, 20, 14, 18, 17]

# Print out the largest and lowst number in the list
print("Largest Number: " + str(max(random_numbers)))
print("Lowest Number: " + str(min(random_numbers)))

# Problem 4-5
# Create a list of multiples of 5 between 1 and 100
multiples_of_5 = list(range(5, 101, 5))

# Print the list of multiples
print(multiples_of_5)

# Problem 4-6
# A list of values from 20 to 30 
numbers_list = list(range(20,31))

# Double each number using list comprehension and print it out
doubled_numbers = [numbers_list * 2 for number in numbers]
print(doubled_numbers)

# Problem 4-7
# Use the list generated in problem 4-4
random_numbers = [5, 10, 6, 1, 9, 7, 2, 11, 3, 8, 4, 12, 15, 13, 19, 16, 20, 14, 18, 17]

# Print the first 2 values
print("First 2 values:")
print(random_numbers[0:3])

# Print items 5-10 in the list
print("Items 5-10:")
print(random_numbers[4:10])

# Print the last 4 items in the list
print("Last 4 items:")
print(random_numbers[-4])

# Problem 4-8
# A list of three favorite musicians/bands 
fav_musicians = ["Oasis", "Dominic Flike", "Mariah Carey"]

# Copy the list into another variable
copied_musicians = fav_musicians.copy()

# Add another musician to the original list
fav_musicians.append("Joji")

# Print both lists
print(fav_musicians)
print(copied_musicians)

# Problem 4-9 
# Store grades in a tuple
grades = ("1st", "2nd", "3rd", "4th", "5th")

# Attempt to modify one of the values using list syntax
=======
# Problem 4-1
# Store favorite places to visit in a list 
favorite_places = ["Beijing", "Tokyo", "Seoul", "Palawan"]

# Use a for loop to print each place in the list with added phrase
for place in favorite_places:
    print(place + " is a nice place to visit.")

# Problem 4-2
# Use a for loop to print the numbers from 90 to 100
for number in range(90,101):
    print(number)

# Problem 4-3
# Create a list of numbers from 100,000 to 1,000,000 
numbers = list(range(100000, 1000001))

# Calculate and print the sum of all numbers
print(sum(numbers))

# Problem 4-4
# Create a list of numbers placed randomly 
random_numbers = [5, 10, 6, 1, 9, 7, 2, 11, 3, 8, 4, 12, 15, 13, 19, 16, 20, 14, 18, 17]

# Print out the largest and lowst number in the list
print("Largest Number: " + str(max(random_numbers)))
print("Lowest Number: " + str(min(random_numbers)))

# Problem 4-5
# Create a list of multiples of 5 between 1 and 100
multiples_of_5 = list(range(5, 101, 5))

# Print the list of multiples
print(multiples_of_5)

# Problem 4-6
# A list of values from 20 to 30 
numbers_list = list(range(20,31))

# Double each number using list comprehension and print it out
doubled_numbers = [numbers_list * 2 for number in numbers]
print(doubled_numbers)

# Problem 4-7
# Use the list generated in problem 4-4
random_numbers = [5, 10, 6, 1, 9, 7, 2, 11, 3, 8, 4, 12, 15, 13, 19, 16, 20, 14, 18, 17]

# Print the first 2 values
print("First 2 values:")
print(random_numbers[0:3])

# Print items 5-10 in the list
print("Items 5-10:")
print(random_numbers[4:10])

# Print the last 4 items in the list
print("Last 4 items:")
print(random_numbers[-4])

# Problem 4-8
# A list of three favorite musicians/bands 
fav_musicians = ["Oasis", "Dominic Flike", "Mariah Carey"]

# Copy the list into another variable
copied_musicians = fav_musicians.copy()

# Add another musician to the original list
fav_musicians.append("Joji")

# Print both lists
print(fav_musicians)
print(copied_musicians)

# Problem 4-9 
# Store grades in a tuple
grades = ("1st", "2nd", "3rd", "4th", "5th")

# Attempt to modify one of the values using list syntax
>>>>>>> b17c380284ed46537583abf047d91d12fea256af
grades[0] = "7th"