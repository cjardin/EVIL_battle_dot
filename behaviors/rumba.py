import random

my_dots = {}

def init():
    return("🚗")


def run(db_cursor , state):
    global my_dots
    #get all my dots
    rows = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
    for row in rows.fetchall():
        if (row[0],row[1]) not in my_dots or (random.random() > .95) :
            my_dots[ (row[0],row[1]) ] = ( random.choice([1,-1]) , random.choice([1,-1]) )
        offset = my_dots[ (row[0],row[1]) ]
        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE')")
        del my_dots[ (row[0],row[1]) ]
        my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset

