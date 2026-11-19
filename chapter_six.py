# Problem 6-1:
# Create a dictionary that stores information about a favorite movie
fav_movie = {'Movie':'Thor:Ragnarok', 'Year Released': '2017', 'Director': 'Taika Waititi', 'Rating': '9/10', 'Genre': ['Action', 'Adventure', 'Sci-Fi', 'Comedy'], 'Runtime': '130min'}

# Problem 6-2:
# Create a dictionary containing product information
product = {'Item Number': '1', 'Product Name': 'PS5', 'Price': 599.99}

# Increase the current price by %30
product['Price'] = product['Price'] * 1.30

# Display a message about the increase of price of the product
print('The price of ', product['Product Name'], 'has increased by %30.')
print(product)

# Problem 6-3:
# Print out all the keys and values from 6-1 dictionary using a loop
for key, value in fav_movie.items():
    print(key, ": ", value)

# Problem 6-4:
# A list of 3 dictionary items, each containing a word and its definition 
words = [{'Word':'Sonder', 'Definition':'The realization that every passerby has a life as vivid and complex as your own.'},
         {'Word':'Ineffable', 'Definition':'Too great, profound, or beautiful to be expressed or described in words.'},
         {'Word':'Wabi-Sabi', 'Definition':'A philosophy of finding beauty in imperfection, impermanence, and simplicity.'}]

# Loop through each item and print out each pair neatly
for word in words:
    print('Word:', word['Word'])
    print('Definition:', word['Definition'])
    print()

# Problem 6-5:
# Add a list of actors/actresses to the existing movie dictionary
fav_movie['Cast'] = ['Chris Hemsworth', 'Tom Hiddleston', 'Mark Ruffalo', 'Tessa Thompson']

for actors in fav_movie['Cast']:
    print(actors)
