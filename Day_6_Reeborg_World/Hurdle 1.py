def turn_right():
    turn_left()
    turn_left()
    turn_left()

def draw_square():
    #Draw Square 
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()

def jump():    
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    jump()



################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
