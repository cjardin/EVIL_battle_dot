import random
import math as m

def update(dna, d_id, state, db_cursor):

    # adds a depleted field to track if an sql table of food can be retrieved.
    # If it can't, then there is no more food left
    if ("depleted" not in state):
        state.update({"depleted": False}) 

    # finds all of the dots that match our id
    my_dot = db_cursor.execute(f"select x,y,owner_id from main_game_field where is_flag = FALSE and d_id = '{d_id}'").fetchall()[0]
    my_dots_id = my_dot[0]

    if state["depleted"]:
        # enemy dots without my id
        rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and owner_id != '{my_dots_id}'")
    else:
        # food has an id of 0, get all of the food
        rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and owner_id = '0'")
        # if rows doesn't update with a new table, then there are no trees left
        if not rows.fetchall():
            state.update({"depleted": True}) # mineral fields depleted
            return

    # helper function to calculate the distance between two vectors
    # d(u, v) = sqrt( (v_1 - u_1)^2 + (v_2 - u2)^2 )
    def calc_distance(src, dest):
        return m.sqrt( ((dest[0] - src[0]) ** 2) + ((dest[1] - src[1]) ** 2) ) 
    
    # get the closest dot
    # keeps crashing when trees deplete
    try:
        closest = rows.fetchall()[0]
    except:
        rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and owner_id != '{my_dots_id}'")
        closest = rows.fetchall()[0]

    # check for nearest food or enemy
    for row in rows.fetchall():
        current_pos = calc_distance(row, my_dot);
        closest_pos = calc_distance(closest, my_dot)
        if current_pos < closest_pos:
            closest = row

    # distance in the x direction
    x_target = closest[0] - my_dot[0]
    # distance in the y direction
    y_target = closest[1] - my_dot[1]

    x_dir = 0
    y_dir = 0

    # determine x direction
    if   x_target > 0: x_dir =  1
    elif x_target < 0: x_dir = -1

    # determine y direction
    if   y_target > 0: y_dir =  1
    elif y_target < 0: y_dir = -1

    db_cursor.execute(f"insert into engine_orders values( {my_dot[0]}, {my_dot[1]}, {my_dot[0] + x_dir }, {my_dot[1] + y_dir }, 'MOVE', '{d_id}')")

