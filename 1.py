import datetime as dt

with open("songs.csv", "r", encoding="utf-8") as f:
    songs = [x.strip().split(";") for x in f.readlines()[1:]]
check_date = dt.datetime.fromisoformat("2002-01-01")  # дата фильтрации
obr_date = dt.datetime.fromisoformat("2023-05-12")  # дата обращения
new_songs = []
for s in songs:
    song = s.copy()
    date = dt.datetime.fromisoformat("-".join(song[-1].split(".")[::-1]))  # перевод даты в тип datetime
    if date < check_date:  # вывод песен по дате выхода не позже 01.01.2002
        print(f"{song[2]} - {song[1]} - {song[0]}")
    if song[0] == "0":  # если нет данных о прослушиваниях
        dlt = obr_date - date
        song[0] = str(int(abs(dlt.days / (len(song[1]) + len(song[2]))) * 10000))
    new_songs.append(song)
with open("songs_new.csv", "w", encoding="utf-8") as f:
    print("streams;artist_name;track_name;date", file=f)
    for song in new_songs:
        print(";".join(song), file=f)