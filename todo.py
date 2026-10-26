tasks = []
while True:
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выход")
    choice = input("Выбор")
    if choice == "1":
        if len(tasks) == 0:
         print("Список пуст")
        else:
            for i, task in enumerate (tasks, start = 1):
                 print(f"{i}. {task}")
    elif choice == "2":
        task=input("Введите задачу")
        tasks.append(task)
    elif choice == "3":
        num=int(input("Выберите задачу: "))
        removed = tasks.pop(num-1)
        print(f"Удалено: {removed}")
    elif choice == "4":
        print("Пока!")
        break
    else:
        print("Неверный выбор")