contacts = {}
while True:
    print("1. Показать все контакты")
    print("2. Добавить контакт")
    print("3. Найти по имени")
    print("4. Удалить контакт")
    print("5. Выход")
    choice = input("Выбор")
    if choice == "1":
       if len(contacts)==0:
           print("Список контактов пуст")
       else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    elif choice == "2":
        name = input("Имя: ")
        phone = input("Телефон: ")
        contacts[name] = phone
    elif choice == "3":
        name = input("Имя: ")
        if name in contacts:
            print(f"Телефон {name}: {contacts[name]}")
        else:
            print(f"{name} не найден")
    elif choice == "4":
        contact = input("Введите контакт")
        if contact in contacts:
            del contacts[contact]
            print(f" Контакт {contact} удален")
        else:
            print("Контакт не найден")
    elif choice == "5":
        print("Пока!")
        break
    else: 
        print("Неверный выбор")
        