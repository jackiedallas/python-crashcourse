def make_album(artist_name, album_title, album_length=None):
    """Return dictionary with with information"""
    album = {'artist': artist_name, 'album': album_title}
    if album_length:
        album['album_length'] = album_length
    return album

while True:
    print("Tell me your favorite music album:")
    print("(Enter 'q' at any time to quit!)")
    
    artist = input("Artist name: ")
    if artist == 'q':
        break
    
    album = input("Album Title: ")
    if album == 'q':
        break
    
    print("Do you know how many tracks are on the album?")
    known_tracks = input("Enter 'y' or 'n': ")
    if known_tracks == 'y':
        num_of_tracks = input("How many tracks are on the album: ")
        new_entry = make_album (artist, album, num_of_tracks)
        print(f"\n{new_entry}")
    elif known_tracks == 'q':
        break
    
    
    new_entry = make_album(artist, album)
    print(f"\n{new_entry}")
