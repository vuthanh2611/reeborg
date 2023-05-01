def step_forward(number):
    for i in range(number):
        move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def L_shape():
    step_forward(3)
    turn_left()
    step_forward(3)
def nex_L_shape():
    turn_right()
    move()
    turn_right()
for i in range(3):
    L_shape()
    nex_L_shape()
L_shape()