import random

def update(dna,d_id,state, db_cursor):
        my_dots = state;
            rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and d_id = '{d_id}'")
                corner = db_cursor.execute(f"SELECT MAX(X), MAX(Y) from main_game_field where is_flag = FALSE and owner_id != '{this_owner_id}'").fetchall()

                    for row in rows.fetchall():
                                src_x = corner[0]
                                        src_y = corner[1]

                                            db_cursor.execute(f"insert into engine_orders values(row[0],row[1],row[0]+dest_x,row[1]+dest_y,'MOVE','{d_id}'")
