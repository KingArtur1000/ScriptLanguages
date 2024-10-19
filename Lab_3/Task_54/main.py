import json
import os


class PhoneBook:
    contactsPath = "Task_54/contacts.json"


    def __init__(self, filename=contactsPath):
        self.filename = filename
        if not os.path.exists(filename):
            self.contacts = {}
            self.save_contacts()
        else:
            self.load_contacts()
    

    def load_contacts(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            self.contacts = json.load(file)
    

    def save_contacts(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.contacts, file, ensure_ascii=False, indent=2)
    

    def search_by_phone(self, phone):
        for name, contact_phone in self.contacts.items():
            if contact_phone == phone:
                return f"Контакт найден: {name}, {phone}"
        return "Контакт не найден"
    

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        self.save_contacts()
        return "Контакт успешно добавлен"
    

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            return "Контакт успешно удален"
        return "Контакт не найден"


def main():
    phone_book = PhoneBook()
    

    while True:
        print("\n1. Поиск по номеру телефона")
        print("2. Добавить контакт")
        print("3. Удалить контакт")
        print("4. Выход")
        
        choice = input("Выберите действие (1-4): ")
        

        match choice:
            case '1':
                phone = input("Введите номер телефона: ")
                print(phone_book.search_by_phone(phone))
            case '2':
                name = input("Введите имя: ")
                phone = input("Введите номер телефона: ")
                print(phone_book.add_contact(name, phone))
            case '3':
                name = input("Введите имя для удаления: ")
                print(phone_book.delete_contact(name))
            case '4':
                break
            case _:
                print("Некорректный выбор, повторите попытку")
        


if __name__ == "__main__":
    main()