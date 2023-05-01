def move_forward(number):
    for _ in range(number):
        if front_is_clear():
            move()
            if object_here():
                take()
for i in range(4):
    move_forward(10)
    turn_left()