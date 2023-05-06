#rain 0
think(50)
def turn_right():
    for _ in range(3):
        turn_left()
def turn_around():
    turn_left()
    turn_left()
for _ in range(6):
    move()
build_wall()
turn_around()
for _ in range(5):
    move()
# rain 1

think(50)


def turn_right():
    for _ in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


move()
turn_right()
move()
while not at_goal():
    move()
    if not front_is_clear():
        turn_left()
    if not wall_on_right() and not at_goal():
        turn_right()
        build_wall()
        turn_left()
# rain3
think(50)


def turn_right():
    for _ in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()

for _ in range(3):
    move()
turn_right()
move()
while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    if not front_is_clear() and wall_on_right():
        turn_left()
    if not wall_on_right() and not at_goal():
        move()
        if wall_on_right():
            turn_around()
            move()
            turn_left()
            build_wall()
            turn_left()
        elif not wall_on_right():
            turn_around()
            move()
            turn_left()
            move()
