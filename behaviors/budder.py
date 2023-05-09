   import random
   import math
   #this is a behavior for budder
   def update(dna, d_id, state,  db_cursor):
       my_dots = state
   
    if("no_food" not in state):
       state.update({"no_food": False})                                                                                                                                                  
       
      if(state["no_food"]):
              
          for row in rows.fetchall():
               if (row[0],row[1]) not in my_dots or (random.random() > .99) :
                  my_dots[ (row[0],row[1]) ] = ( random.choice([1,-1]) , random.choice([1,-1]) )                                                                                        
              offset = my_dots[ (row[0],row[1]) ]
              db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE', '{d_id}')")
              del my_dots[ (row[0],row[1]) ]
              my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset
              
           else:
              trees = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and owner_id = '0'")
              trees.fetchall()
              if(not trees):
                  state.update({"no_food": True})
                  return
                  