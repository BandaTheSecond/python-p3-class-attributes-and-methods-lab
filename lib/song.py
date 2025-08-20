class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre, year=None):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.year = year

        # Increment song count
        Song.count += 1

        # Tracking genres and artists'
        Song.genres.append(genre)
        Song.artists.append(artist)

        # Updating histograms
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls):
        """Return unique genres"""
        return list(set(cls.genres))

    @classmethod
    def add_to_artists(cls):
        """Return unique artists"""
        return list(set(cls.artists))

    @classmethod
    def add_to_genre_count(cls, genre):
        """Update genre histogram"""
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        """Update artist histogram"""
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

#Songs
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Lose Yourself", "Eminem", "Rap", 2002)
song3 = Song("Hey Jude", "The Beatles", "Rock")
song4 = Song("Ring of Fire", "Johnny Cash", "Country", 1963)
song5 = Song("Mockingbird", "Eminem", "Rap", 2004)

print("Song count:", Song.count)  
print("Genres list (raw):", Song.genres)  
print("Unique genres:", Song.add_to_genres())  
print("Artists list (raw):", Song.artists)  
print("Unique artists:", Song.add_to_artists())  
print("Genre count:", Song.genre_count)  
print("Artist count:", Song.artist_count)  
