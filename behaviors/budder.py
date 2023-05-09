  1 import random
  2 import math
  3 #this is a behavior for budder
  4 def update(dna, d_id, state,  db_cursor):
  5     my_dots = state
  6 
  7     if("no_food" not in state):
  8     state.update({"no_food": False})                                                                                                                                                  
  9     
 10     if(state["no_food"]):
 11             
 12         for row in rows.fetchall():
 13              if (row[0],row[1]) not in my_dots or (random.random() > .99) :
 14                 my_dots[ (row[0],row[1]) ] = ( random.choice([1,-1]) , random.choice([1,-1]) )                                                                                        
 15             offset = my_dots[ (row[0],row[1]) ]
 16             db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
 17             del my_dots[ (row[0],row[1]) ]
 18             my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset
 19             
 20          else:
 21             trees = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and owner_id = '0'")
 22             trees.fetchall()
 23             if(not trees):
 24                 state.update({"no_food": True})
 25                 return
 26                 