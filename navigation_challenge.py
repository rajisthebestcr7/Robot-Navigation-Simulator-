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

goal_x = 3
goal_y = 3

print("Welcome to Raj's Robot Navigation Simulator!")
print("The robot starts at position (0, 0).")
print("Goal Position:", (goal_x, goal_y))

while True:

    if x == goal_x and y == goal_y:
        print("\nMission Complete!")
        print("The robot reached the goal.")
        print("Total Moves:", moves)
        break

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
