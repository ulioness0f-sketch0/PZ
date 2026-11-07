# Смоделировать простейший калькулятор, умеющий выпонять 4 основные арифметические операции.
while True:
    try:
        x1 = int(input("Введите первое число: "))
        op = input("Введите операцию: ")
        x2 = int(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка!")
summ = 0
vichet = 0
umnog = 0
delen = 0
if op == "+":
    summ = x1 + x2
    print(summ)
elif op == "-":
    vichet = x1 - x2
    print(vichet)
elif op == "*":
    umnog = x1 * x2
    print(umnog)
elif op == ":":
    delen = x1 / x2
    print(delen)
else:
    print("Ошибка!")