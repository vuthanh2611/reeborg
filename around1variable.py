def go_circle():
    while True:
        while front_is_clear():
            move()
            if object_here():
                done()
        turn_left()
put()
move()
go_circle()