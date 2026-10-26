a = float(input("Введите первое число: "))
b = float(input("Введите второе число: ")) 
opr = input("Операция (+, -, *, /): ")
def add (a, b):
    return a + b
           
def substract (a, b):
     return a-b
    
def multiply (a, b):
     return a * b
 
def divide (a, b):
     
     if b == 0:
        return "Ошибка: "
     return a / b
    

if opr == "+":
   result=add(a,b)
elif opr == "-":
    result=substract(a,b)
elif opr == "*":
    result=multiply(a,b)
elif opr == "/":
    result=divide(a,b)
else:
    result = ("Неверное значение")
print(f"Результат: {result}")
   