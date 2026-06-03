# navigation_challenge.py
# Author: Raj Modi
# Date: June 2026
# Description:
# A robot navigation simulator that allows users to move a robot
# through a simple grid. The robot must avoid obstacles and reach
# the goal position while tracking the total number of moves made.

x = 0
y = 0
moves = 0

goal_x = 3
goal_y = 3

obstacles = [
    (2, 0),
    (1, 2)
]

print("Welcome to Raj's Robot Navigation Simulator!")
print("Starting Position:", (x, y))
print("Goal Position:", (goal_x, goal_y))
print("Obstacle Positions:", obstacles)

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

    new_x = x
    new_y = y

    if command == "up":
        new_y += 1

    elif command == "down":
        new_y -= 1

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

    if (new_x, new_y) in obstacles:
        print("Obstacle detected. Move blocked.")

    else:
        x = new_x
        y = new_y
        moves += 1
        print("Robot moved successfully.")
