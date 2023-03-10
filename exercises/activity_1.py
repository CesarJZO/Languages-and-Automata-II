import math
#1, -3, 2
#1, -2, 1

def quadratic_equation(a, b, c):
    x1 = (-b + math.sqrt(b**2 - 4 * a *c)) / 2 * a
    x2 = (-b - math.sqrt(b**2 - 4 * a *c)) / 2 * a
    print("X1:", x1, "| X2:", x2)

def hypotenuse():
    base=float(input("Da la base del triangulo: "))
    altura=float(input("Da la altura del traingulo: "))
    hipotenusa = math.sqrt((base**2)+(altura**2))
    print("la hipotenusa del traigulo rectangulo es ", str(hipotenusa))

def cylinder_volume(height, radius):
    volume = height * math.pi * radius ** 2
    print(f"Volume: {volume:.2f}")

menu = """
1. Calculate quadratic equation
2. Calculate hypotenuse
3. Calculate volume of a cylinder
4. Exit
"""
opt = (int)(input(menu))
while opt != 4:
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
