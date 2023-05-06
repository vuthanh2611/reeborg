#token1
hink(50)


def turn_right():
    for _ in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()


def move_object():
    move()
    while object_here():
        take()
    toss()


move_object()
while not at_goal():
    move()
