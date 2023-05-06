think(100)


def turn_right():
    for _ in range(3):
        turn_left()


def harvest_one_row():
    for _ in range(5):
        take()
        move()


def change_right_direction():
    take()
    turn_right()
    move()
    turn_right()


def change_left():
    take()
    turn_left()
    move()
    turn_left()


def move_foward(num):
    for _ in range(num):
        move()


move_foward(2)
turn_left()
move_foward(2)
for i in range(6):
    harvest_one_row()
    if i % 2 == 0:
        change_right_direction()
    else:
        change_left()




