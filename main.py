import turtle

print("Программа по визуализации фракталов\n"
      "Елин Лев v0.1\n"
      "***\n"
      "Доступные фракталы:\n"
      "(Первым идёт название фрактала, вторым его номер)\n"
      "***\n"
      "Кривая Дракона - 1\n")
name_fr_list = [1]
name_fr = int(input("Введите номер фрактала: "))
while name_fr not in name_fr_list:
    print("Ошибка, Неверный номер фрактала!")
    name_fr = str(input("Введите номер фрактала: "))
iterations = int(input("Введите целое число, количество итераций фрактала меньше 20: "))
if iterations >= 20:
    iterations = 19
it_count = iterations
speed = input("Введите целое число, скорость робота: ")
tur = turtle.Turtle()
tur.speed(int(speed))

dragon_fr_rot = ""


def help_dragon_fr(n, d="R"):
    global dragon_fr_rot
    if n == 1:
        pass
    else:
        help_dragon_fr(n-1, "R")
        dragon_fr_rot += d
        help_dragon_fr(n-1, "L")


def dragon_fr(iteration):
    global dragon_fr_rot
    help_dragon_fr(iteration)
    n = 10
    if iteration > 5:
        n = 5
    elif iteration > 8:
        n = 2
    elif iteration > 15:
        n = 0.1
    for i in dragon_fr_rot:
        if i == "R":
            tur.forward(n)
            tur.left(-90)
        else:
            tur.forward(n)
            tur.left(90)


tur.getscreen().bgcolor("black")
tur.color("cyan")
tur.penup()
tur.goto((0, 0))
tur.pendown()

if name_fr == 1:
    dragon_fr(iterations)

turtle.done()
