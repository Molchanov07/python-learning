num = int(input("Введите число: "))
if num < 0 or num > 100:
    print("Некорректное значение")
elif num >= 90 and num <= 100:
    print("Отлично")
elif num >= 75 and num <= 89:
    print("Хорошо")
elif num >= 60 and num <= 74:
    print("Удовлетворительно")
else:
    print("Неудовлетворительно")