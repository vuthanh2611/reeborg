think(50)
def turn_right():
    for _ in range(3):
        turn_left()
def move_to_goal():
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

move_to_goal()
