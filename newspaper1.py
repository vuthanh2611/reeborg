
think(50)
def turn_right():
    for _ in range(3):
        turn_left()
def three_steps():
    move()
    turn_right()
    move()
    move()
    turn_left()
def three_steps_down():
    move()
    move()
    turn_left()
    move()
    turn_right()
def up_three_steps():
    for _ in range(3):
        three_steps()
def down_three_steps():
    for _ in range(3):
        three_steps_down()
take()
turn_left()
up_three_steps()
put()
while object_here('token'):
    take('token')
turn_left()
down_three_steps()