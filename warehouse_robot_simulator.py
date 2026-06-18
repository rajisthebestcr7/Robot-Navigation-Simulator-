# warehouse_robot_simulator.py
# Author: Raj Modi
# Description:
# A warehouse robot simulator where a robot moves through
# a warehouse, avoids obstacles, picks up a package,
# and delivers it to the delivery zone.

robot_x = 0
robot_y = 0

moves = 0
package_picked = False

package_location = (1, 2)
delivery_zone = (4, 4)

obstacles = [
    (3, 0),
    (3, 1),
    (2, 4)
]

def display_warehouse(x, y):

    print("\nWarehouse Map:")

    for row in range(5):

        for col in range(5):

            if (col, row) == (x, y):
                print("R", end=" ")

            elif (col, row) == package_location and not package_picked:
                print("P", end=" ")

            elif (col, row) == delivery_zone:
                print("D", end=" ")

            elif (col, row) in obstacles:
                print("X", end=" ")

            else:
                print(".", end=" ")

        print()

print("Welcome to the Warehouse Robot Simulator!")

while True:

    display_warehouse(robot_x, robot_y)

    print("\nCurrent Position:", (robot_x, robot_y))
    print("Moves Made:", moves)

    if package_picked:
        print("Package Status: Picked Up")
    else:
        print("Package Status: Not Picked Up")

    command = input(
        "\nEnter command (up, down, left, right, quit): "
    ).lower()

    new_x = robot_x
    new_y = robot_y

    if command == "up":
        new_y -= 1

    elif command == "down":
        new_y += 1

    elif command == "left":
        new_x -= 1

    elif command == "right":
        new_x += 1

    elif command == "quit":
        print("\nSimulation ended.")
        break

    else:
        print("Invalid command.")
        continue

    if new_x < 0 or new_x > 4 or new_y < 0 or new_y > 4:
        print("Boundary reached. Move blocked.")
        continue

    if (new_x, new_y) in obstacles:
        print("Obstacle detected. Move blocked.")
        continue

    robot_x = new_x
    robot_y = new_y

    moves += 1

    print("Robot moved successfully.")

    if (robot_x, robot_y) == package_location and not package_picked:

        package_picked = True

        print("\nPackage picked up successfully!")

    if (robot_x, robot_y) == delivery_zone and package_picked:

        print("\nDelivery Complete!")
        print("The package was delivered successfully.")
        print("Total Moves:", moves)

        break 
