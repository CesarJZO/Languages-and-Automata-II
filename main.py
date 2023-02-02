import math

def quadratic_equation(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4 * a *c)) / 2 * a
    x2 = (-b - math.sqrt(b**2 - 4 * a *c)) / 2 * a
    print("X1: ", x1, ", X2: ", x2)

def cylinder_volume(height, radius):
    volume = height * math.pi * radius ** 2
    print(f"Volume: {volume}")

menu = """
1. Calculate quadratic equation
2. Calculate hypotenuse
3. Calculate volume of a cylinder
"""
opt = (int)(input(menu))

if opt == 1:
    a = (float)(input("a: "))
    b = (float)(input("b: "))
    c = (float)(input("c: "))
    quadratic_equation(a, b, c)

elif opt == 2:
    hypotenuse()
elif opt == 3:
    height = (float)(input("Height: "))
    radius = (float)(input("Radius: "))
    cylinder_volume(height, radius)
