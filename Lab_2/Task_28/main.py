def append_to_file(filename, text):
    try:
        with open(filename, 'a') as file:
            file.write(text)
    except FileNotFoundError:
        print("Ошибка: файл не найден!")
    except IOError:
        print("Ошибка: не удалось открыть или сохранить файл!")

append_to_file('Task_28/task_28.txt', 'Hello, world!\n')