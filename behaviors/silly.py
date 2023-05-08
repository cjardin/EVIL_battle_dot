import random
# a very silly dot 
def update(dna, d_id, state, db_cursor):
    my_dots = state
    prob = 0.50
    x_direction = 1  # starting direction along the x-axis
    y = 0  # starting y-coordinate
    frame_count = 0  # counter for current frame number
    rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and  d_id = '{d_id}'")
    for row in rows.fetchall():
        if (row[0], row[1]) not in my_dots or (random.random() < prob):
            if frame_count % 2 == 0:
                # simulating a zigzag motion
                # even frames
                x = row[0] + x_direction
                my_dots[(row[0], row[1])] = (x, row[1])
            else:
                # in odd frames, add 1 to y value
                my_dots[(row[0], row[1])] = (row[0], y)
                y += 1
            frame_count += 1
        offset = my_dots[(row[0], row[1])]
        db_cursor.execute(f"insert into engine_orders values({row[0]}, {row[1]}, {row[0] + offset[0]}, {row[1] + offset[1]}, 'MOVE', '{d_id}')")
        del my_dots[(row[0], row[1])]
        my_dots[(row[0] + offset[0], row[1] + offset[1])] = offset

