# Берём из файла список артистов и запихиваем их в массив
with open("Task_24/artists.txt", "r") as file:
    music_groups = [line.strip() for line in file]

# Выводим в консоль
for group in music_groups:
    print(group)
