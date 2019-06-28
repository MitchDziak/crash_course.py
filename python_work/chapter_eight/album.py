def make_album(artist, album, tracks=0):
    album = {
        'name': artist.title(), 
        'title': album.title(),
        }
    if tracks:
        album['tracks'] = tracks
    return album
    
while True:
    artist = input("Please input the artist: ")
    if artist == 'q':
        break
        
    album = input("Please input the album: ")
    if album == 'q':
        break
        
    check = input("Do you know the # of tracks? (y/ no) ")
    if check == 'y':
        tracks = input("Please input the # of tracks: ")
    elif check == 'q':
        break
        
    
    output = album + " by " + artist + "\n"
    
    print(output)
    
    
