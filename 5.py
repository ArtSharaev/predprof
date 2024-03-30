with open("songs.csv", "r", encoding="utf-8") as f:
    songs = [x.strip().split(";") for x in f.readlines()[1:]]

unique_tracks = []
unique_songs = []
for song in songs:  # отсеивание повторяющихся треков
    if song[2] not in unique_tracks:
        unique_songs.append(song)
table = dict()
for song in unique_songs:  # заполнение хэш-таблицы
    artist = song[1]
    try:
        table[artist] += 1
    except KeyError:
        table[artist] = 1
popular = list(sorted(table.keys(), key=lambda x: table[x],
                      reverse=True))  # сортировка списка артистов по количеству треков хэш-таблице
for i in range(10):  # вывод первых 10-ти артистов
    print(f"{popular[i]} выпустил {table[popular[i]]} песен.")
