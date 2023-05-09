import numpy as np
import random
# if losing change food id from 0 to anything else will kill most all other curr programs and me // cutting losses
#def hunt(me_coords, prey_coords):
 #   my_xy = np.array(me_coords[:2])
  #  prey_xys = np.array([coord[:2] for coord in prey_coords])
   # deltas = prey_xys - my_xy
   # distances = np.einsum('ij,ij->i', deltas, deltas)
   # closest_index = np.argmin(distances)
   # return prey_coords[closest_index]
   # direction = np.array(closest_prey[:2]) - my_xy
   # step = direction / np.linalg.norm(direction)
    #return tuple(step)
    #old version of hunt below is untested 5/7
    #prey=np.asarray(prey)
    #deltas= nodes-node
    #dist_2 =np.einsum(('ij,ij->i',deltas,deltas)
    #return np.unravel_index(np.argmin(prey),prey.shape)
    #xy=prey[:2]
   # deltas=xy-me[:2]
  #  dist_2 = np.einsum('ij,ij->i',deltas,deltas)
 #   return np.unravel_index(np.argmin(dist_2),dist_2.shape)
### cutting losseessss
def update(dna, d_id, state,  db_cursor):
    my_dots = state
    rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and  d_id = '{d_id}'")
    for row in rows.fetchall():
        if (row[0],row[1]) not in my_dots or (random.random() > .95) :
            my_dots[ (row[0],row[1]) ] = ( random.choice([1,-1]) , random.choice([1,-1]) )
        offset = my_dots[ (row[0],row[1]) ]
        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
        del my_dots[ (row[0],row[1]) ]
        my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset
   # my_dots = state
   # me = db_cursor.execute(f"select x,y,owner_id from main_game_field where is_flag = FALSE and d_id = '{d_id}'").fetchall()[0]#should fetch the first row in the db but also the only row 
   # my_id=me[2] 
   # prey=db_cursor.execute(f"select x,y,owner_id from main_game_field where is_flag = FALSE and owner_id= '0' ").fetchall()
   # if len(prey)==0:
       # db_cursor.execute(f"update  from main_game_field where is_flag = FALSE and d_id = '{d_id}'")
    #    prey=db_cursor.execute(f"select x,y,owner_id from main_game_field where is_flag = FALSE and owner_id != '{my_id}'").fetchall()
    #index=hunt(me,prey)## make athe smallest whole number step 
    #diff
    

  #  db_cursor.execute(f"insert into engine_orders values( {me[0]}, {me[1]}, {me[0] }, {me[1] }, 'MOVE', '{d_id}')")
   # del my_dots[ (me[0],me[1]) ]
  #  my_dots[ (me[0] + scent[0], me[1]  scent[1]) ] = scent# idk if scent is good to equal but i guess 

    

    ##   if (prey[0],prey[1]) not in my_dots or (random.random() > .95) :
      ## offset = my_dots[ (prey[0],prey[1]) ]
        #db_cursor.execute(f"insert into engine_orders values( {prey[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
        #del my_dots[ (row[0],row[1]) ]
        #my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset
  