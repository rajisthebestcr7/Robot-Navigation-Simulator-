# navigation_challenge.py
# Author: Raj Modi
# Date: June 2026
# Description:
# Robot Navigation Simulator with manual navigation,
# automatic navigation, multiple maps, scoring,
# obstacle detection, and difficulty levels.

moves = 0

print("Welcome to Raj's Robot Navigation Simulator!")

print("\nSelect Difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty = input("Enter 1, 2, or 3: ")

if difficulty == "1":
    goal = (4, 4)
    obstacles = [(2, 0), (1, 2)]
    difficulty_name = "Easy"

elif difficulty == "2":
    goal = (4, 4)
    obstacles = [(1, 1), (2, 1), (3, 2), (1, 3)]
    difficulty_name = "Medium"

elif difficulty == "3":
    goal = (4, 4)
    obstacles = [(1, 0), (1, 1), (2, 2), (3, 2)]
    difficulty_name = "Hard"

else:
    print("Invalid selection.")
    quit()

x = 0
y = 0


def display_grid(robot_x, robot_y):
    print("\nDifficulty:", difficulty_name)
    print("Grid Map:")

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


print("\nChoose Navigation Mode:")
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
        print("Difficulty:", difficulty_name)
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
            break

        else:
            print("Invalid command.")
            continue

    elif mode == "2":

        if x < goal[0] and (x + 1, y) not in obstacles:
            new_x += 1

        elif y < goal[1] and (x, y + 1) not in obstacles:
            new_y += 1

        elif x > goal[0] and (x - 1, y) not in obstacles:
            new_x -= 1

        elif y > goal[1] and (x, y - 1) not in obstacles:
            new_y -= 1

        else:
            print("No safe automatic move available.")
            break

        print("Auto Navigation Mode Active")

    else:
        print("Invalid mode selected.")
        break

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
