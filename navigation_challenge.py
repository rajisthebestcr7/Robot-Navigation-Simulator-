# navigation_challenge.py
# Author: Raj Modi
# Date: June 2026
# Description:
# A robot navigation simulator where the user controls a robot through
# a grid while avoiding obstacles and reaching a goal position.
# The simulator tracks movement, displays a visual map, and calculates
# a score based on navigation efficiency.

x = 0
y = 0
moves = 0

goal = (4, 4)

obstacles = [
    (2, 0),
    (1, 2),
    (3, 3)
]

def display_grid(robot_x, robot_y):
    print("\nGrid Map:")

    for row in range(5):
        for col in range(5):

            if (col, row) == (robot_x, robot_y):
                print("R", end=" ")

            elif (col, row) == goal:
                print("G", end=" ")

            elif (col, row) in obstacles:
                print("X", end=" ")

            else:
                print(".", end=" ")

        print()

print("Welcome to Raj's Robot Navigation Simulator!")

while True:

    display_grid(x, y)

    if (x, y) == goal:

        score = 100 - (moves * 5)

        if score < 0:
            score = 0

        print("\nMission Complete!")
        print("Total Moves:", moves)
        print("Efficiency Score:", score)
        break

    print("\nCurrent Position:", (x, y))
    print("Moves Made:", moves)

    command = input(
        "Enter a command (up, down, left, right, quit): "
    ).lower()

    new_x = x
    new_y = y

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
        print("Final Position:", (x, y))
        print("Total Moves:", moves)
        break

    else:
        print("Invalid command. Please try again.")
        continue

    if new_x < 0 or new_x > 4 or new_y < 0 or new_y > 4:
        print("Boundary reached. Move blocked.")
        continue

    if (new_x, new_y) in obstacles:
        print("Obstacle detected. Move blocked.")
        continue

    x = new_x
    y = new_y
    moves += 1

    print("Robot moved successfully.")
