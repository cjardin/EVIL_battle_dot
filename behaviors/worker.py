import random

def update(dna, d_id, state,  db_cursor):
    rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and  d_id = '{d_id}'")
    random_direction = random.choice([0])
        db_cursor.execute(f"insert into engine_orders values( {rows[0]}, {rows[1]}, {rows[0] + random_direction }, {rows[1] + random_direction }, 'MOVE', '{d_id}')")