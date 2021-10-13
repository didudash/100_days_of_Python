def turn_right():
    turn_left()
    turn_left()
    turn_left()  

def wall_jump_var():
    turn_left()
    while not right_is_clear() and not wall_in_front() and not at_goal():
        move()
        if right_is_clear():
            turn_right()
            move()
            turn_right()
            move()

while front_is_clear() and not at_goal():
    move()
while wall_in_front() and not at_goal():
    wall_jump_var()
 
  
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
