with open("songs.csv", "r", encoding="utf-8") as f:
    songs = [x.strip().split(";") for x in f.readlines()[1:]]

russian_artists = set()
foreign_artists = set()
russian_letters = "ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"  # список всех русских букв
for song in songs:
    name = song[1]  # получение имени артиста
    is_russian = False
    for letter in name:  # проверка каждой буквы в имени артиста
        if letter in russian_letters:  # добавление к российским артистам
            russian_artists.add(name)
            is_russian = True
            break
    if not is_russian:  # добавление к иностранным артистам
        foreign_artists.add(name)
print(f"Количество российских исполнителей: {len(russian_artists)}")
with open("russian_artists.txt", "w", encoding="utf-8") as f:
    for name in russian_artists:
        print(name, file=f)
print(f"Количество иностранных исполнителей: {len(foreign_artists)}")
with open("foreign_artists.txt", "w", encoding="utf-8") as f:
    for name in foreign_artists:
        print(name, file=f)