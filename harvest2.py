think(100)


def take_carrot():
    while object_here():
        take()


def turn_right():
    for _ in range(3):
        turn_left()


def harvest_one_row():
    for _ in range(6):
        take_carrot()
        move()


def change_right_direction():
    take_carrot()
    turn_right()
    move()
    turn_right()


def change_left():
    take_carrot()
    turn_left()
    move()
    turn_left()


def move_foward(num):
    for _ in range(num):
        move()


def initial():
    move_foward(2)
    turn_left()
    move_foward(2)


initial()
for i in range(6):
    harvest_one_row()
    if i % 2 == 0:
        change_right_direction()
    else:
        change_left()




