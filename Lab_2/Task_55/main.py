import random


def guess_the_number():
    number = random.randint(1, 10)
    attempts = 0

    while True:
        try:
            guess = int(input("Угадайте число от 1 до 10 --> "))
        except ValueError:
            print("Неверный ввод! Пожалуйста, введите целое число.")
            continue
        else:
            break

    attempts += 1

    while guess != number:
        if guess < number:
            print("Попробуй число побольше :)")
        elif guess > number:
            print("Попробуй число поменьше :)")

        try:
            guess = int(input("Попробуй ещё раз: "))
            attempts += 1
            continue
        except ValueError:
            print("Неверный ввод! Пожалуйста, введите целое число.")
            continue

    print(f"Поздравляю! Вы угадали число {number} за {attempts} попыток!")


guess_the_number()
