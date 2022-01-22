import turtle

print("Программа по визуализации фракталов\n"
      "Елин Лев v0.1\n"
      "***\n"
      "Доступные фракталы:\n"
      "(Превым идёт название фрактала, вторым его имя в программе)\n"
      "***\n"
      "Кривая Дракона - dragon_fr\n")
name_fr_list = ["dragon_fr"]
name_fr = str(input("Введите имя фрактала: "))
while name_fr not in name_fr_list:
    print("Ошибка, Неверное имя фрактала!")
    name_fr = str(input("Введите имя фрактала: "))

iterations = int(float(input("Введите целое число, колличество итераций фрактала меньше 20: ")))
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

if name_fr == "dragon_fr":
    dragon_fr(iterations)


turtle.done()
