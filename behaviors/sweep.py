import random

def update(dna, d_id, state,  db_cursor):
    n = -1
    for c in d_id:
        try:
            n = (int)(c)
            break
        except:
            pass
    if n == -1:
        n = random.randint(0,1)
    rando = random.random()
    if n%2 == 0:
        if rando > .1:
            dir = -1
        else:
            dir = 1
    else:
        if rando > .1:
            dir = 1
        else:
            dir = -1
    my_dots = state
    rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and  d_id = '{d_id}'")
    for row in rows.fetchall():
        if (row[0],row[1]) not in my_dots:
            my_dots[ (row[0],row[1]) ] = ( dir , random.choice([1,-1]) )
        offset = my_dots[ (row[0],row[1]) ]
        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
        del my_dots[ (row[0],row[1]) ]
        my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset

