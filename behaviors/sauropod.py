import random

def update(dna, d_id, state,  db_cursor):
    my_dots = state
    rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and  d_id = '{d_id}'")
    for row in rows.fetchall():
        if (row[0],row[1]) not in my_dots or (random.random() > .95) :
            my_dots[ (row[0],row[1]) ] = ( random.choice([0,1,-1]) , random.choice([0,1,-1]) )
        offset = my_dots[ (row[0],row[1]) ]
          
        # collide with width
        if (row[1] + offset[1] >= 30):
            offset = (1, random.choice([0,1]))
        # invert on collision
        if (row[1] + offset[1] < 0):
            offset = (1, random.choice([0,1]))
        # collision with height 
        if (row[0] + offset[0] >= 50):
            offset = (1, random.choice([0,1]))
        # invert on collision 
        if (row[0] + offset[0] < 0):
            offset = (1, random.choice([0,1]))


        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
        del my_dots[ (row[0],row[1]) ]
        my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset