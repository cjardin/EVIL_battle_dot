#https://asciimatics.readthedocs.io/en/stable/io.html#creating-a-screen

from random import randint,shuffle
from asciimatics.screen import Screen
import time
import yaml

import random

import sqlite3

from glob import glob
import importlib
import sys
import os

import logging

import json
import uuid

import traceback


dot_objects = {}
def get_new_dot(dna):
    did = str(uuid.uuid4())
    dot_objects[did] = {}
    return did 



#Creating and Configuring Logger

Log_Format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.ERROR)

logger = logging.getLogger()

#Testing our Logger

logger.error("Our First Log Message")


configs = None
with open('battleDots.yml', 'r') as file:
    configs  = yaml.safe_load(file)

#del the db each play
try:
    os.unlink(configs['env']['dbfile'])
except:
    pass

con = sqlite3.connect(configs['env']['dbfile'])

GAME_WIDTH = configs['env']['width']
GAME_HEIGHT = configs['env']['height']

cur = con.cursor()
for sql in configs['sql']['setup']:
    cur.execute(sql)

for i in range( int( (GAME_WIDTH * GAME_HEIGHT) * configs['env']['food_amount'])):
    cur.execute(configs['sql']['place_food'].replace('!!X', str(randint(0,GAME_WIDTH))).replace('!!Y', str(randint(0,GAME_HEIGHT)) ))

good_players = []
for g in glob(configs['env']['player_dir'], recursive = True):
    try:
        dot_dna = {}
        with open(g, 'rb') as f:
            dot_dna = json.loads(f.read())

        init_pos = (randint(0,GAME_WIDTH), randint(0,GAME_HEIGHT))
        p ={  "name" : dot_dna['dot_name'], "dot_char": dot_dna['dot_emoji'],
            "flag_x_y" : init_pos, "init_pos" : init_pos,
            "state" : {
                        "MAX_X" : GAME_WIDTH,
                        "MAX_Y" : GAME_HEIGHT,
                        "NAME"  : dot_dna['dot_name'],
                        "DNA"   : dot_dna
                    } 
        }
        
        good_players.append(p)
        cur.execute( configs['sql']['del_initl_pos'].replace('!!X', str( init_pos[0]  )).replace('!!Y', str(init_pos[1])))
        cur.execute( configs['sql']['new_player'].replace("!!id", str( len(good_players) )).replace( "!!name", dot_dna['dot_name']).replace("!!char", 
                    dot_dna['dot_emoji'])  )
        cur.execute( configs['sql']['set_flag'].replace('!!X', str( init_pos[0]  )).replace('!!Y', str(init_pos[1])).replace('!!_name', dot_dna['dot_name']))
        cur.execute( configs['sql']['set_initial_pos'].replace('!!X', str( init_pos[0]  )).replace('!!Y',
                str(init_pos[1])).replace('!!_name', dot_dna['dot_name']).replace("!!UUID", get_new_dot(dot_dna) ))
    except Exception as ex:
        print(ex)
        print( traceback.format_exc())
        sys.exit()

print(good_players)
sys.exit()

def demo(screen):
    while True:
        screen.clear()
        for row in cur.execute(configs['sql']['get_all_screen_to_print']):
            screen.print_at(row[2] , row[0], row[1], colour=7)
        screen.refresh()

        shuffle(good_players)
        for p in good_players:
            p['module'].run(cur, p['state'])
    
            cur.execute(configs['sql']['get_move_actions'].replace('!!max_x', str(GAME_WIDTH)).replace('!!max_y', str(GAME_HEIGHT) ))
            actions = cur.fetchall()
            for row in actions:
                skip_insert = False
                #should be in the yml.. but I miss f :)
                cur.execute(f"select name, is_flag from main_game_field as a, owner b  where a.owner_id = b.owner_id and X = {row[0]} and Y = {row[1]}")
                collisions = cur.fetchall()
                for c_row in collisions:
                    if c_row[0] == 'Food':
                        cur.execute(f"insert into main_game_field values ( {p['flag_x_y'][0]}, {p['flag_x_y'][1]}, (select owner_id from owner where name='{p['module_name']}') , FALSE)")
                        cur.execute(f"delete from main_game_field where X = {row[0]} and Y = {row[1]} and owner_id = (select owner_id from owner where name='Food') ")
                    elif c_row[0] == p['module_name']:
                        #we bouncs
                        pass
                    elif c_row[1] == 1:
                        #Got a FLAG!!!
                        print(111)
                    else:
                        #combat 50/50 chance of winning :)
                        if random.choice( [True, False]):
                            skip_insert = True
                            cur.execute(f"delete from main_game_field where owner_id = (select owner_id from owner where name='{p['module_name']}')  and X = {row[0]} and Y = {row[1]} and is_flag = FALSE")
                        else:
                            cur.execute(f"delete from main_game_field where owner_id = (select owner_id from owner where name='{c_row[0]}')  and X = {row[0]} and Y = {row[1]} and is_flag = FALSE")

                    
                if skip_insert == False:
                    cur.execute(f"update main_game_field set X = {row[2]} , Y = {row[3]} where owner_id = (select owner_id from owner where name='{p['module_name']}') and X = {row[0]} and Y = {row[1]} and is_flag = FALSE")
            cur.execute("delete from engine_orders")
        time.sleep(.1)
        con.commit()

Screen.wrapper(demo)

