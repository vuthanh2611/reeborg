think(50)


def turn_right():
    for _ in range(3):
        turn_left()


def go_circle():
    while not object_here():
        if not front_is_clear():
            turn_left()
        if right_is_clear():
            turn_right()
        move()


put()
turn_left()
turn_left()
move()
go_circle()


