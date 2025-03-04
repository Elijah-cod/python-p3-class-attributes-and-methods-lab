class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.genres.append(genre)
        Song.artists.append(artist)
        Song.add_to_genre_count()
        Song.add_to_artist_count()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    
    @classmethod
    def add_to_genres(cls):
        return set(cls.genres)

    @classmethod
    def add_to_artists(cls):
        return set(cls.artists)
    
    @classmethod
    def add_to_genre_count(cls):
        for item in cls.genres:
            if item in cls.genre_count:
                cls.genre_count[item] += 1 
            else:
                cls.genre_count[item] = 1 
    
    @classmethod
    def add_to_artist_count(cls):
        for artist in cls.artists:
            if artist in cls.artist_count:
                cls.artist_count[artist] += 1 
            else:
                cls.artist_count[artist] = 1 