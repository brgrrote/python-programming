# ==============================================================
# Problem 8-1:    
# ==============================================================  
# A function of my favorite radio station                                                
def fav_radio(station):
    print("Let me tune in " + station + ".")

fav_radio("Virgin Radio Dubai")

# Allow user to input favorite radio station and store 
user_radio = input("Input your favorite radio station: ")
fav_radio (user_radio)                                   

# ==============================================================
# Problem 8-2:
# ==============================================================
# A function that contain information of a business card
def print_business_cards(name, quantity, tagline):
    print("Printing " + str(quantity) + " business cards for " + name + " ,with the tagline: " + tagline)

# Call the function three times
print_business_cards("Brianna", 100, "For a better future.")
print_business_cards("Kaizen", 80, "Driven by vision.")
print_business_cards("Rae", 180, "Continuous growth, every single day.")

# ==============================================================
# Problem 8-3:
# ==============================================================
# Modify the function in problem 8-2 to make quantity default to 100
def print_business_cards(name, tagline, quantity=100):
    print("Printing " + str(quantity) + " business cards for " + name + " with the tagline: " + tagline)

# Call the function twice, with one exceeding the default value. 
print_business_cards("Brianna", "For a better future.", 150)
print_business_cards("Kaizen", "Driven by vision.")

# ==============================================================
# Problem 8-4 :
# ==============================================================
# A function containing song information, with artist set to 'Unknown'
def song_info(title, artist='Unknown'):
    return title + " by " + artist + "."

# Call the function three times
print (song_info("Why", "Dominic Flike"))
print (song_info("Incomplete"))
print (song_info("Sway"))

# ==============================================================
# Problem 8-5:
# ==============================================================
# Modified function returning a dictionary instead of a string
def song_info(title, artist='Unknown'):
    song = {"title": title, "artist": artist}
    return song

def print_playlist(playlist):
    print("Your Playlist")
    for song in playlist:
        print(song["title"] + " by " + song["artist"] + ".")

# Empty list and while loop to collect user input
playlist = []

while True:
    print("Enter song details (or type 'q' to quit):")
    title = input("Song title: ")
    if title.lower()=='q':
        break

    artist = input("Artist name (press Enter if unknown): ")
    if artist.lower()=='q':
        break

    # Use default 'Unknown' if the user left the artist blank
    if artist == "":
        new_song = song_info(title)
    else:
        new_song = song_info(title, artist)

    # Add to the playlist
    playlist.append(new_song)

# Pass the completed list to the print function 
print_playlist(playlist)