<<<<<<< HEAD
# Problem 3-1
# A list of the last 4 books read 
books = ["Atomic Habits", "The Old Fire", "1984", "The Alchemist"]

# Print each book individually in title case
print("I just read: " + books[0].title())
print("I just read: " + books[1].title())
print("I just read: " + books[2].title())
print("I just read: " + books[3].title())

# Problem 3-2
# Create a list of top 4 favorite shows
fav_show = ["VisionQuest", "Daredevil: Born Again", "Love Other Than Yours", "All of Us Are Dead"]

# Replace the show that got cancelled with a new favorite show
fav_show[3] = "The Last of Us"

# Add a new favorite show using append 
fav_show.append("The Punisher")

# Insert a new favorite show without being positioned at the first or last index
fav_show.insert(2, "Nine to Six")

# Remove the last show using pop() and print it out
print(fav_show.pop())

# Remove the first three shows using del
del fav_show[0:3]

# Print the final list 
print(fav_show)

# Problem 3-3
# Store a list of travel destinations
travel_destinations = ["Tokyo", "Palawan", "Beijing", "Paris", "New York"]

# Find the number of items in the list
print(len(travel_destinations))

# Sort the list in alphabetical order 
travel_destinations.sort()
print (travel_destinations)

# Display the list in reverse without changing the original list
print(sorted(travel_destinations, reverse=True))

# Reverse the order of the list
travel_destinations.reverse()
print(travel_destinations)

# Problem 3-4
# Write a code that has an indexing error 
avengers = ["Iron Man", "Thor", "Black Widow", "Hulk", "Captain America"]

print(avengers[5]) # This will cause an error as there is no index 5 in the list, the last index is 4

# Fixed Code 
# print(avengers[4]) This corrected code will print "Captain America"
=======
# Problem 3-1
# A list of the last 4 books read 
books = ["Atomic Habits", "The Old Fire", "1984", "The Alchemist"]

# Print each book individually in title case
print("I just read: " + books[0].title())
print("I just read: " + books[1].title())
print("I just read: " + books[2].title())
print("I just read: " + books[3].title())

# Problem 3-2
# Create a list of top 4 favorite shows
fav_show = ["VisionQuest", "Daredevil: Born Again", "Love Other Than Yours", "All of Us Are Dead"]

# Replace the show that got cancelled with a new favorite show
fav_show[3] = "The Last of Us"

# Add a new favorite show using append 
fav_show.append("The Punisher")

# Insert a new favorite show without being positioned at the first or last index
fav_show.insert(2, "Nine to Six")

# Remove the last show using pop() and print it out
print(fav_show.pop())

# Remove the first three shows using del
del fav_show[0:3]

# Print the final list 
print(fav_show)

# Problem 3-3
# Store a list of travel destinations
travel_destinations = ["Tokyo", "Palawan", "Beijing", "Paris", "New York"]

# Find the number of items in the list
print(len(travel_destinations))

# Sort the list in alphabetical order 
travel_destinations.sort()
print (travel_destinations)

# Display the list in reverse without changing the original list
print(sorted(travel_destinations, reverse=True))

# Reverse the order of the list
travel_destinations.reverse()
print(travel_destinations)

# Problem 3-4
# Write a code that has an indexing error 
avengers = ["Iron Man", "Thor", "Black Widow", "Hulk", "Captain America"]

print(avengers[5]) # This will cause an error as there is no index 5 in the list, the last index is 4

# Fixed Code 
# print(avengers[4]) This corrected code will print "Captain America"
>>>>>>> b17c380284ed46537583abf047d91d12fea256af
