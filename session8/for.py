songs = ['lala', 'hello', 'hehe']

# for i in range(len(songs)):
#     print(songs[i])

# for song in songs:
#     print(song)

new1 = input("new songs: ", )
new2 = input("new songs: ", )
new3 = input("new songs: ", )

songs.append(new1)
songs.append(new2)
songs.append(new3)

for i, song in enumerate(songs):
    print(i, song. upper())

