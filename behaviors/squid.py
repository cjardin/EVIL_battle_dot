import random

def update(dna, d_id, state,  db_cursor):
    my_dots = state
    rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and  d_id = '{d_id}'")
    for row in rows.fetchall():
        # conditions for movement, check where other dots are and avoid
        if ((row[1],row[1]) not in my_dots) and ((row[-1],row[-1]) not in my_dots) and ((row[0],row[1]) not in my_dots) and ((row[0],row[-1]) not in my_dots) and
            ((row[1],row[0]) not in my_dots) and ((row[-1],row[0]) not in my_dots):
            my_dots[ (row[0],row[0]) ] = (random.choice([1,0,-1]) , random.choice([1,0,-1]) )
        elif (row[0],row[1]) not in my_dots or ((row[0],row[-1]) not in my_dots):
            my_dots[ (row[1],row[0]) ] = ( random.choice([1,0,-1]) , 0 )
        elif (row[1],row[0]) not in my_dots or ((row[-1],row[0]) not in my_dots):
            my_dots[ (row[0],row[1]) ] = ( 0 , random.choice([1,0,-1]) )
        else:
            my_dots[ (row[1],row[1]) ] = ( random.choice([1,-1]) , random.choice([1,-1]) )
        offset = my_dots[ (row[0],row[1]) ]
        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
        del my_dots[ (row[0],row[1]) ]
        my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset
