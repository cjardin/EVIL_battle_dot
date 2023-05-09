import random

def update(dna, d_id, state, db_cursor):
    my_dots = state

    this_dot = db_cursor.execute(f"select x,y,owner_id from main_game_field where is_flag = FALSE and d_id = '{d_id}'").fetchall()[0]
    this_owner_id = this_dot[2]
   
    number_of_allies = db_cursor.execute(f"select count(*) from main_game_field where is_flag = FALSE and owner_id = '{this_owner_id}'").fetchone()[0]
    number_of_enemies = db_cursor.execute(f"select count(*) from main_game_field where is_flag = FALSE and owner_id != '0' and owner_id != '{this_owner_id}'").fetchone()[0]

    rows = db_cursor.execute(f"SELECT x, y FROM main_game_field WHERE is_flag = FALSE AND d_id = '{d_id}'")
    for row in rows.fetchall():
        if number_of_allies < number_of_enemies:
            if (row[0],row[1]) not in my_dots or (random.random() > .8) :
                my_dots[ (row[0],row[1]) ] = ( random.choice([1,-1]) , random.choice([1,-1]) )
            offset = my_dots[ (row[0],row[1]) ]
            db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
            del my_dots[ (row[0],row[1]) ]
            my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset
        else:
            db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + random.choice([0,1,-1]) }, {row[1] + random.choice([0,1,-1]) }, 'MOVE', '{d_id}')")