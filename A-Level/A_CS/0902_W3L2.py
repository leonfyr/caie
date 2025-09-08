# Homework 5 & 6

import math

# Constants
maxHeight = 25
maxWidth = 30

# Input height
while True:
    height = float(input("Please enter the height: "))
    if 0 < height <= maxHeight:
        break

# Input width
while True:
    width = float(input("Please enter the width: "))
    if 0 < width <= maxWidth:
        break

# Menu
print("Please select the value you want to calculate:")
print("1. Hypotenuse 2. Area 3. Perimeter")
option = int(input())

if option == 1:
    hypotenuse = math.sqrt(height ** 2 + width ** 2)
    print("Hypotenuse:", hypotenuse)
elif option == 2:
    area = height * width / 2
    print("Area:", area)
elif option == 3:
    hypotenuse = math.sqrt(height ** 2 + width ** 2)
    print("Perimeter:", height + width + hypotenuse)
else:
    print("Invalid option")