import math

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
    quadratic_equation()
elif opt == 2:
    hypotenuse()
elif opt == 3:
    height = (float)(input("Height: "))
    radius = (float)(input("Radius: "))
    cylinder_volume(height, radius)
