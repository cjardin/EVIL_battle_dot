import random

def update(dna, d_id, state, db_cursor):
    my_dots = state
    rows = db_cursor.execute(f"SELECT x, y FROM main_game_field WHERE is_flag = FALSE AND d_id = '{d_id}'")
    for row in rows.fetchall():
        if (row[0], row[1]) not in my_dots:
            my_dots[(row[0], row[1])] = (random.choice([-1, 0, 1]), random.choice([-1, 0, 1]))
        offset = my_dots[(row[0], row[1])]

        # check if dot is at an edge
        if (row[0] + offset[0] < 0 or row[0] + offset[0] >= 250 or
                row[1] + offset[1] < 0 or row[1] + offset[1] >= 50):
            offset = (random.choice([-1, 0, 1]), random.choice([-1, 0, 1]))

        db_cursor.execute(f"INSERT INTO engine_orders VALUES ({row[0]}, {row[1]}, {row[0] + offset[0]}, {row[1] + offset[1]}, 'MOVE', '{d_id}')")
        del my_dots[(row[0], row[1])]
        my_dots[(row[0] + offset[0], row[1] + offset[1])] = offset

