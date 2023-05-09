import random

def update(dna, d_id, state,  db_cursor):
    my_jdots = state
    rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and  d_id = '{d_id}'")
    for row in rows.fetchall():
        if (row[0],row[1]) not in my_jdots or (random.random() > .75) :
            my_jdots[ (row[0],row[1]) ] = ( random.choice([-1,1]) , random.choice([-1,1]) )
        offset = my_jdots[ (row[0],row[1]) ]
        #higher chance to stay in location to defend
        if row[0] + offset[0] >= 50 and row[1] + offset[1] <= 50 and (random.random() > .50):
            my_jdots[ (row[0],row[1]) ] = ( random.choice([0,-1]) , random.choice([0,-1]) )
        else:
            my_jdots[ (row[0],row[1]) ] = ( random.choice([1,0]), random.choice([1,0]) )
        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
        del my_jdots[ (row[0],row[1]) ]
        my_jdots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset