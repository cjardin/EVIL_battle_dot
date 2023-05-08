import random

def update(dna, d_id, state,  db_cursor):
    my_dots = state
    rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and  d_id = '{d_id}'")
    for row in rows.fetchall():
        if (row[0],row[1]) not in my_dots or (random.random() > .5) :
            # my_dots[ (row[0],row[1]) ] = ( random.choice([1,-1]) , random.choice([1,-1]) ) ]   <----original movement from rumba
            #restrict the bot's movements to only vertical or horizontal directions, so less spasm-y
            #it also goes diagonal, when the tuple is two non-zero values. Otherwise, it goes horiz. or vert.
            my_dots[ (row[0],row[1]) ] = ( random.choice([0,1])*random.choice([-1,1]), random.choice([0,1])*random.choice([-1,1]))
        offset = my_dots[ (row[0],row[1]) ]
        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
        del my_dots[ (row[0],row[1]) ]
        my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset
