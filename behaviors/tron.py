import random

def update(dna, d_id, state,  db_cursor):
    my_dots = state
    rows = db_cursor.execute(f"SELECT * FROM main_game_field WHERE '🌳' = '{d_id}' AND is_flag = FALSE")
    for row in rows.fetchall():
        if (row[0], row[1], row[2], row[4]) not in my_dots or (random.random() > .50) :
            my_dots[(row[1],row[1])] = ( random.choice([4,-1]) , random.choice([1,0]) )
        offset = my_dots[ (row[1],row[-1]) ]
        db_cursor.execute(f"INSERT INTO engine_orders VALUES( {row[1]}, {row[1]}, {row[2] + offset[1] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
