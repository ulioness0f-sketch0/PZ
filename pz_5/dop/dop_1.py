# Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод результата предусмотреть в основной программе. Расчет суммы цифр оформить в функции.
def schetchik(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total
while True:
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        break
    except ValueError:
        print("Ошибка")


summ_a = schetchik(a)
summ_b = schetchik(b)
summ_c = schetchik(c)


if summ_a >= summ_b and summ_a >= summ_c:
    print(a)
elif summ_b >= summ_a and summ_b >= summ_c:
    print(b)
else:
    print(c)