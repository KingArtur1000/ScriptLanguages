def write_favorite_poem(filename):
    # Записываем в файл любимое стихотворение
    with open(filename, 'w', -1, "utf-8") as f:
        f.write("""
Ибо, кто возвышает себя, 
тот унижен будет,
а кто унижает себя,
тот возвысится.
    Евангелие от Матфея 23:12
                """)

def read_and_count_vowels(filename):
    # Прочтите стихотворение из файла и подсчитайте количество гласных в начале каждой строки
    with open(filename, 'r', -1, "utf-8") as f:
        lines = f.readlines()
        
    vowel_counts = {'Гласные': 0, 'Согласные': 0}

    for i, line in enumerate(lines):
        # Не учитываем регистр букв
        line = line.strip().lower()

        print(f"\tСтрока №{i+1} {line}")
        # Првоеряем каждое слово в строке с какой буквы оно начинается: гласной или согласной
        for word in line.split():
            if line and word[0] in 'аоуыеёиэюя':
                vowel_counts['Гласные'] += 1
            elif line and word[0] in 'бвгдежзийклмнопрстуфхцчшщъыьэюя':
                vowel_counts['Согласные'] += 1
                print(f"Слово {word} начинается с согласной")

    return vowel_counts


# Записываем стихотворение в файл 'poem.txt'
filename = 'Task_52/poem.txt'
write_favorite_poem(filename)


# Считываем из него стихотворение и проверяем сколько слов начинается на гласные и согласные буквы
vowel_counts = read_and_count_vowels(filename)
print(f"Число слов начинающихся на {vowel_counts}")
