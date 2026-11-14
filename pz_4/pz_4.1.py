# Даны два целых числа A и B (A < B). Найти сумму всех целых чисел от A до B включительно.
while True:
    try:
        A = int(input("Введите A: "))
        B = int(input("Введите B: "))
        if A >= B:
            print("Ошибка! A должно быть меньше B")
        else:
            summ = 0
    
        while A <= B:
            summ += A
            A += 1
        print("Сумма: ", summ)
    except ValueError:
        print("Ошибка! Нужно ввести целые числа")
