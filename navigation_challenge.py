# navigation_challenge.py
# Author: Raj Modi
# Date: June 2026
# Description:
# My first robot navigation simulator. This project combines concepts
# from my earlier Python projects, including user input, variables,
# loops, and decision-making. The user controls a robot and moves it
# around a simple grid while tracking its position.

x = 0
y = 0
moves = 0

print("Welcome to Raj's Robot Navigation Simulator!")
print("The robot starts at position (0, 0).")

while True:
    print("\nCurrent Position:", (x, y))

    command = input(
        "Enter a command (up, down, left, right, quit): "
    ).lower()

    if command == "up":
        y += 1
        moves += 1
        print("Robot moved up.")

    elif command == "down":
        y -= 1
        moves += 1
        print("Robot moved down.")

    elif command == "left":
        x -= 1
        moves += 1
        print("Robot moved left.")

    elif command == "right":
        x += 1
        moves += 1
        print("Robot moved right.")

    elif command == "quit":
        print("\nSimulation ended.")
        print("Final Position:", (x, y))
        print("Total Moves:", moves)
        break

    else:
        print("Invalid command. Please try again.")


