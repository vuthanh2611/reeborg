
think(50)
def turn_right():
    for _ in range(3):
        turn_left()
def move_to_goal():
    while not at_goal():
        if  wall_in_front():
            turn_left()
        if right_is_clear():
            turn_right()
        move()
move_to_goal()
