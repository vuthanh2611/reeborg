think(50)
def turn_right():
    for _ in range(3):
        turn_left()
count = 0
while front_is_clear() and not wall_in_front():
    move()
    count += 1
turn_left()
turn_left()
for _ in range(count//2):
    move()
put()
