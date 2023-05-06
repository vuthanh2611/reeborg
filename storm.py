#storm1
think(50)


def turn_right():
    for _ in range(3):
        turn_left()


def turn_around():
    turn_left()
    turn_left()

for i in range(5):
    move()
    while object_here():
        take()
turn_around()
for i in range(5):
    move()
turn_right()
while carries_object():
    toss()
done()

