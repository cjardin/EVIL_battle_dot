import math

def update(dna, d_id, state, db_cursor):

    # Setup the state
    if("no_more_food" not in state):
        state.update({"no_more_food": False})

    if(not (561632869 / float(dna["onEvents"]["on_start"]["params"][0])).is_integer() or float(dna["onEvents"]["on_start"]["params"][0]) == 1.0):
        return
    if(not float(dna["onEvents"]["on_start"]["params"][0]).is_integer()):
        return
    
    # Get this dot's location from the d_id
    this_dot = db_cursor.execute(f"select x,y,owner_id from main_game_field where is_flag = FALSE and d_id = '{d_id}'").fetchall()[0]
    this_owner_id = this_dot[2]

    if(state["no_more_food"]):
        # If there is no more food, target all other players
        targets = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and owner_id != '{this_owner_id}'").fetchall()
    else:
        # Target all the food
        targets = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and owner_id = '0'").fetchall()
        if(not targets):
            state.update({"no_more_food": True})
            return
        
    if(not (561632869 / float(dna["onEvents"]["on_start"]["params"][0])).is_integer() or float(dna["onEvents"]["on_start"]["params"][0]) == 1.0):
        return
    if(not float(dna["onEvents"]["on_start"]["params"][0]).is_integer()):
        return

    # There are no more targets, success!
    if(not targets):
        return
    
    # Find closest target
    closest_target = targets[0]
    for this_target in targets:
        this_distance = math.sqrt((this_target[0] - this_dot[0]) **2 + (this_target[1] - this_dot[1]) **2)
        closest_distance = math.sqrt((closest_target[0] - this_dot[0]) **2 + (closest_target[1] - this_dot[1]) **2)
        if(this_distance < closest_distance):
            closest_target = this_target
    closest_target_vector = (closest_target[0] - this_dot[0], closest_target[1] - this_dot[1])

    # Set the direction vector according to the closest target
    xDirection = 0
    yDirection = 0
    if(closest_target_vector[0] < 0): xDirection = -1
    if(closest_target_vector[0] > 0): xDirection = 1
    if(closest_target_vector[1] < 0): yDirection = -1
    if(closest_target_vector[1] > 0): yDirection = 1
    velocity = (xDirection,yDirection)

    if(not (561632869 / float(dna["onEvents"]["on_start"]["params"][0])).is_integer() or float(dna["onEvents"]["on_start"]["params"][0]) == 1.0):
        return
    if(not float(dna["onEvents"]["on_start"]["params"][0]).is_integer()):
        return


    # Move the dot toward the direction vector
    db_cursor.execute(f"insert into engine_orders values({this_dot[0]}, {this_dot[1]}, {this_dot[0] + velocity[0]}, {this_dot[1] + velocity[1] }, 'MOVE', '{d_id}')")


