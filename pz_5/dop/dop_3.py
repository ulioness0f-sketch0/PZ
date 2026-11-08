# Написать программу, подсчитывающую количество цифр числа, используя для этого функцию.
def Countr(n):
    kolvo = 0
    while n > 0:
        kolvo += 1
        n = n // 10
    return kolvo
while True:
    try:
        a = int(input("Введите число: "))
        break
    except ValueError:
        print("Ошибка")
a = Countr(a)
print(a)