import turtle

print("Программа по визуализации фракталов\n"
      "Елин Лев v0.2\n"
      "***\n"
      "Доступные фракталы:\n"
      "(Превым идёт название фрактала, вторым его имя в программе)\n"
      "***\n"
      "Кривая Дракона - dragon_fr\n")
name_fr_list = ["dragon_fr"]
#name_fr = str(input("Введите имя фрактала: "))
#while name_fr not in name_fr_list:
#    print("Ошибка, Неверное имя фрактала!")
#    name_fr = str(input("Введите имя фрактала: "))

#iterations = int(float(input("Введите целое число, колличество итераций фрактала: ")))
#it_count = iterations
speed = input("Введите целое число, скорость робота: ")
tur = turtle.Turtle()
tur.speed(int(speed))

tur.getscreen().bgcolor("black")
tur.color("cyan")
tur.penup()
tur.goto((0, 0))
tur.pendown()


dragon_fr_per = 1

#def dragon_fr(iteration):
#    while True:
#        if it_count == 0:
#           return


turtle.done()