# this file moves a dot in a vertical, horizontal, diagonal direction
# TODO: remove diagonal

import random

# my guess is that the update method just puts the new coordinates in the state when
# the dot(s) move(s)
def update(dna, d_id, state,  db_cursor):
    my_dots = state
    rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and  d_id = '{d_id}'")
  # for all rows on the map, map size 210 x 50
    for row in rows.fetchall():
      # if there are no dots in either (0,1) or the spawnpoint I'm guessing
      # or
      # random "chance of happening" float is .95
        if (row[0],row[1]) not in my_dots or (random.random() > .95) :
          # move dots
            my_dots[ (row[0],row[1]) ] = ( random.choice([1,-1]) , random.choice([1,-1]) )
        offset = my_dots[ (row[0],row[1]) ]
        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
      # delete where the dots once were (?)  
        del my_dots[ (row[0],row[1]) ]
        my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset

