import random
import math
#my behav idk what im doing lol

food_targeted = {}

def update(dna, d_id, state,  db_cursor):
    my_dots = state
    rows = db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and d_id = '{d_id}'")

    for row in rows.fetchall():
        if(row[0], row[1]) not in my_dots or (row[0], row[1]) == my_dots[(row[0], row[1])]:
            my_dots[(row[0], row[1])] = findFood(db_cursor, row[0], row[1])

        goto = my_dots[(row[0], row[1])]
        if goto != ():
            offset = getOffset(row[0], row[1], goto[0], goto[1]) 
        else:
            offset = (random.choice([1,-1]), random.choice([1,-1])) 

        if(row[0] + offset[0], row[1] + offset[1]) not in my_dots: 
            db_cursor.execute(f"insert into engine_orders values({row[0]}, {row[1]}, {row[0] + offset[0]}, {row[1] + offset[1]}, 'MOVE', '{d_id}')")
            my_dots[(row[0] + offset[0], row[1] + offset[1])] = goto
        else:
            my_dots[(row[0], row[1])] = goto

#find food
def findFood(db_cursor, x, y):
    global food_targeted
    foodTarget = ()
    mDistance = 9999

    #find stuff marked food
    for food in db_cursor.execute(f"select x,y from main_game_field where is_flag = FALSE and owner_id = (select owner_id from owner where name='Food')").fetchall():
        distance = abs(math.dist([food[0], food[1]], [x, y]))
        if distance < mDistance and distance != 0 and (food[0], food[1]) not in food_targeted:
            foodTarget = (food[0], food[1])
            mDistance = distance
            
    food_targeted[foodTarget] = 1
    return foodTarget


#gets offset between two points
def getOffset(fromX, fromY, toX, toY):
    offset = [0,0]

    if (toX - fromX) < 0: offset[0] = -1
    elif (toY - fromY) > 0: offset[0] = 1

    if (toY - fromY) < 0: offset[1] = -1
    elif (toY - fromY) > 0: offset[1] = 1

    return offset