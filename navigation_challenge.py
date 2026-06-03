# navigation_challenge.py
# Author: Raj Modi
# Date: June 2026
# Description:
# A robot navigation simulator where users can control a robot
# manually or allow it to navigate automatically. The simulator
# includes obstacle avoidance, boundary detection, a visual grid,
# move tracking, and an efficiency score.

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
print("\nChoose a mode:")
print("1. Manual Navigation")
print("2. Auto Navigation")

mode = input("Enter 1 or 2: ")

while True:

    display_grid(x, y)

    if (x, y) == goal:

        score = 100 - (moves * 5)

        if score < 0:
            score = 0

        print("\nMission Complete!")
        print("The robot reached the goal.")
        print("Total Moves:", moves)
        print("Efficiency Score:", score)
        break

    print("\nCurrent Position:", (x, y))
    print("Moves Made:", moves)

    new_x = x
    new_y = y

    if mode == "1":

        command = input(
            "Enter a command (up, down, left, right, quit): "
        ).lower()

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

    elif mode == "2":

        if x < goal[0]:
            new_x += 1

        elif x > goal[0]:
            new_x -= 1

        elif y < goal[1]:
            new_y += 1

        elif y > goal[1]:
            new_y -= 1

        print("Auto Navigation: Robot selected its next move.")

    else:
        print("Invalid mode selected.")
        break

    if new_x < 0 or new_x > 4 or new_y < 0 or new_y > 4:
        print("Boundary reached. Move blocked.")
        continue

    if (new_x, new_y) in obstacles:
        print("Obstacle detected. Move blocked.")

        if mode == "2":
            if y < goal[1]:
                new_y = y + 1
                new_x = x

                if (new_x, new_y) not in obstacles and new_y <= 4:
                    x = new_x
                    y = new_y
                    moves += 1

        continue

    x = new_x
    y = new_y
    moves += 1

    print("Robot moved successfully.")
