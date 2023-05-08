import random

#This behavior will not update the position of the dot, remaining in place (good for defensive play).

def update(dna, d_id, state,  db_cursor):
    my_dots = state
    rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and  d_id = '{d_id}'")
    for row in rows.fetchall():
        if (row[0],row[1]) not in my_dots or (random.random() > .95) :
            my_dots[ (row[0],row[1]) ] = ( random.choice([1,-1]) , random.choice([1,-1]) )
        

