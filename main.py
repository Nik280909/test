a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
operation = input("Введите операцию")

if (operation == '+'):
    print("Результат:" + str(a + b))
elif (operation == '-'):
    print("Результат: " + str(a - b))
elif (operation == '*'):
    print("Результат: " + str(a * b))
elif (operation == '/'):
    print("Результат: " + str(a / b))
else:
    print("ошибка")