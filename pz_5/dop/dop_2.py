# Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в функции.
def Perimetr(a, b, c, d):
    return a + b + c + d
def Ploshad(a, b):
    return a * b
while True:
    try:
        v = int(input("Введитее верхнюю сторону: "))
        n = int(input("Введитее нижнюю сторону: "))
        l = int(input("Введитее левую сторону: "))
        p = int(input("Введитее правую сторону: "))
        break
    except ValueError:
        print("Ошибка")

perimetr = 0
ploshad = 0
if v <= 0 or l <= 0 or n <= 0 or p <= 0:
    print("Длина не может быть отрицательной")
elif v != n or l != p:
    print("Параллельные стороны должны быть равны")
else:
    perimetr = Perimetr(v, l, n, p)
    print(perimetr)
    ploshad = Ploshad(v, l)
    print(ploshad)