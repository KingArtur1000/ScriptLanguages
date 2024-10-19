import random

filePath = 'Task_53/theater.txt'

def create_theater_file(rows, seats_per_row=15):
    # Создаем матрицу случайных мест (0 или 1)
    theater = [[random.randint(0, 1) for _ in range(seats_per_row)] for _ in range(rows)]
    
    # Записываем в файл
    with open(filePath, 'w') as f:
        for row in theater:
            f.write(' '.join(map(str, row)) + '\n')


def count_free_seats():
    free_seats = 0
    with open(filePath, 'r') as f:
        for line in f:
            free_seats += line.strip().count('0')
    return free_seats


def check_seat(row, seat):
    with open(filePath, 'r') as f:
        theater = [line.strip().split() for line in f]
        
    if 0 <= row - 1 < len(theater) and 0 <= seat - 1 < len(theater[0]):
        status = theater[row-1][seat-1]
        return "свободно" if status == '0' else "занято"
    else:
        return "недопустимые номера места или ряда"


def main():
    # Запрашиваем возраст для расчета количества рядов
    parent_age = int(input("Введите возраст одного из родителей: "))
    student_age = int(input("Введите ваш возраст: "))
    rows = parent_age - student_age
    
    # Создаем файл с местами
    create_theater_file(rows)
    
    while True:
        print("\n1. Показать количество свободных мест")
        print("2. Проверить место")
        print("3. Выход")
        
        choice = input("\tВыберите действие (1-3): ")
        
        if choice == '1':
            print(f"Свободных мест: {count_free_seats()}")
        elif choice == '2':
            row = int(input("Введите номер ряда: "))
            seat = int(input("Введите номер места: "))
            print(f"Статус места: {check_seat(row, seat)}")
        elif choice == '3':
            break


if __name__ == "__main__":
    main()