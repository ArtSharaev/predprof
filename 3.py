with open("songs.csv", "r", encoding="utf-8") as f:
    songs = [x.strip().split(";") for x in f.readlines()[1:]]
request = input()
while request != "0":  # считывание запросов ведется до ввода "0" пользователем
    was_find = False
    for song in songs:  # линейный поиск артистов
        if song[1] == request:  # проверка имени артиста на совпадение с запросом
            print(f"У {song[1]} найдена песня: {song[2]}")
            was_find = True
            break
    if not was_find:  # проверка на то, был ли найден артист
        print("К сожалению, ничего не удалось найти")
    request = input()