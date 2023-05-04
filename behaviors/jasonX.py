import random

def update(dna, d_id, state,  db_cursor):
        #get all my dots
        rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and  d_id = '{d_id}'")
        for row in rows.fetchall():
            db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[2]}, {row[0] + random.choice([0,1,-2]) }, {row[2] + random.choice([0,1,-2]) }, 'MOVE', '{d_id}')")