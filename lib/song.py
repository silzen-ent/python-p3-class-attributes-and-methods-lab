class Song:
    
    count = 0            # Class variable to keep track of the total number of Song objects
    genres = []          # Class variable to store all unique genres
    artists = []         # Class variable to store all unique artists
    genre_count = {}     # Class variable to store count of songs for each genre
    artist_count = {}    # Class variable to store count of songs for each artist

    def __init__(self, name, artist, genre):
        self.name = name                  # Instance variable to store song name
        self.artist = artist              # Instance variable to store artist name
        self.genre = genre                # Instance variable to store genre
        self.add_song_to_count()          # Method call to increment the total count of Song objects
        self.add_to_genres(genre)        # Method call to add the genre to the genres list
        self.add_to_artists(artist)      # Method call to add the artist to the artists list
        self.add_to_genre_count(genre)   # Method call to update the count of songs for the given genre
        self.add_to_artist_count(artist) # Method call to update the count of songs for the given artist
    
    @classmethod 
    def add_song_to_count(cls):
        cls.count += 1    # Increment the total count of Song objects

    @classmethod
    def add_to_genres(cls, new_genre):
        if new_genre not in cls.genres:
            cls.genres.append(new_genre)  # Add the new genre to the genres list if it doesn't already exist

    @classmethod
    def add_to_artists(cls, new_artist):
        if new_artist not in cls.artists:
            cls.artists.append(new_artist)  # Add the new artist to the artists list if it doesn't already exist

    @classmethod
    def add_to_genre_count(cls, new_genre):
        if new_genre not in cls.genre_count:
            cls.genre_count[new_genre] = 1  # If the genre doesn't exist in the genre count dictionary, initialize its count to 1
        else:
            cls.genre_count[new_genre] += 1  # Increment the count of songs for the given genre

    @classmethod
    def add_to_artist_count(cls, new_artist):
        if new_artist not in cls.artist_count:
            cls.artist_count[new_artist] = 1  # If the artist doesn't exist in the artist count dictionary, initialize its count to 1
        else:
            cls.artist_count[new_artist] += 1  # Increment the count of songs for the given artist