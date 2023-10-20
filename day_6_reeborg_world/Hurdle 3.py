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
    

#while at_goal() == False:
    #jump()
def wall_jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
   
#wall_jump()
#wall_jump()

while not at_goal():
    if wall_in_front():
        wall_jump()
    else:
        move()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
