# navigation_challenge.py
# Author: Raj Modi
# Date: June 2026
# Description:
# Robot Navigation Simulator with manual navigation,
# automatic navigation, multiple difficulty levels,
# obstacle detection, scoring, improved pathfinding,
# and navigation statistics.

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
    print("Invalid difficulty selected.")
    quit()

x = 0
y = 0
mission_success = False


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


def is_safe(position):
    x_pos, y_pos = position

    if x_pos < 0 or x_pos > 4:
        return False

    if y_pos < 0 or y_pos > 4:
        return False

    if position in obstacles:
        return False

    return True


def show_dashboard():
    score = 100 - (moves * 5)

    if score < 0:
        score = 0

    print("\n==============================")
    print("NAVIGATION STATISTICS")
    print("==============================")
    print("Difficulty:", difficulty_name)
    print("Mission Success:", mission_success)
    print("Total Moves:", moves)
    print("Efficiency Score:", score)
    print("Goal Position:", goal)
    print("Final Position:", (x, y))
    print("==============================")


print("\nChoose Navigation Mode:")
print("1. Manual Navigation")
print("2. Auto Navigation")

mode = input("Enter 1 or 2: ")

while True:

    display_grid(x, y)

    if (x, y) == goal:

        mission_success = True

        print("\nMission Complete!")
        print("The robot reached the goal.")

        show_dashboard()
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
            print("\nSimulation ended by user.")
            show_dashboard()
            break

        else:
            print("Invalid command.")
            continue

    elif mode == "2":

        print("Auto Navigation Mode Active")

        possible_moves = [
            (x + 1, y),
            (x, y + 1),
            (x - 1, y),
            (x, y - 1)
        ]

        best_move = None
        best_distance = 999

        for move in possible_moves:

            if is_safe(move):

                distance = (
                    abs(move[0] - goal[0]) +
                    abs(move[1] - goal[1])
                )

                if distance < best_distance:
                    best_distance = distance
                    best_move = move

        if best_move is None:
            print("No safe path found.")
            show_dashboard()
            break

        new_x, new_y = best_move

    else:
        print("Invalid mode selected.")
        break

    if not is_safe((new_x, new_y)):
        print("Move blocked.")
        continue

    x = new_x
    y = new_y
    moves += 1

    print("Robot moved successfully.")
