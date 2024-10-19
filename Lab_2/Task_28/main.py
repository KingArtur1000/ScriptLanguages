def write_to_file(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text)
            print("Текст успешно записан в файл.")
    except FileNotFoundError:
        print(filename)
        print("Ошибка: файл не найден!")
    except IOError:
        print("Ошибка: не удалось открыть или сохранить файл!")

write_to_file('task_28.txt', "Hello, world!\n")
