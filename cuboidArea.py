# Filename: cuboidArea.py
# Created by: Brady Collier
# Date created: 01/13/19
# Description: Calculates the length, height, depth, and surface area of a cuboid.

# Main Function


def cuboid():
    # Prompts user to enter x,y,z values
    x_1 = int(input("Enter a value for x_1: "))
    y_1 = int(input("Enter a value for y_1: "))
    z_1 = int(input("Enter a value for z_1: "))
    x_2 = int(input("Enter a value for x_2: "))
    y_2 = int(input("Enter a value for y_2: "))
    z_2 = int(input("Enter a value for z_2: "))
    x_3 = int(input("Enter a value for x_3: "))
    y_3 = int(input("Enter a value for y_3: "))
    z_3 = int(input("Enter a value for z_3: "))
    x_4 = int(input("Enter a value for x_4: "))
    y_4 = int(input("Enter a value for y_4: "))
    z_4 = int(input("Enter a value for z_4: "))

    # Calculates the length, height, depth, and surface area by taking the difference in provided values
    length = x_2 - x_1
    height = y_2 - y_3
    depth = z_3 - z_4
    surface_area = (((length * height) * 2) + ((length * depth) * 2) + ((depth * height) * 2))

    # Prints the length, height, depth, and surface area on screen
    print("Length of the cuboid: %.2f" % length)
    print("Height of the cuboid: %.2f" % height)
    print("Depth of the cuboid: %.2f" % depth)
    print("Surface area of the cuboid: %.2f" % surface_area)


cuboid()