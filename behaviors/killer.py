import random

class killer:
    def __init__(self, data):
        self.data = data

    def update(self, db_cursor, state):
        #get all my dots
        rows = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
        for row in rows.fetchall():
            db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + random.choice([0,1,-1]) }, {row[1] + random.choice([0,1,-1]) }, 'MOVE')")

