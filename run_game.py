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
import time


from dot_actor import dot_actor

#Creating and Configuring Logger
Log_Format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.DEBUG)

logger = logging.getLogger()
#Testing our Logger
logger.debug("Game start")


#load configs
configs = None
with open('battleDots.yml', 'r') as file:
    configs  = yaml.safe_load(file)


#load the database
#del the db each play
try:
    os.unlink(configs['env']['dbfile'])
except:
    pass
con = sqlite3.connect(configs['env']['dbfile'])

GAME_WIDTH = configs['env']['width']
GAME_HEIGHT = configs['env']['height']


#------------------------------------------
dot_objects = {}
dot_score_board = {}
def get_new_dot(dna, dot_name):
    did = str(uuid.uuid4())
    dot_objects[did] = dot_actor(dna, did)

    if dot_name not in dot_score_board:
        dot_score_board[dot_name] = {
            "kills" : 0,
            "food" : 0,
            "alive" : 1
        }
    return did 


def setup_game():
    cur = con.cursor()
    for sql in configs['sql']['setup']:
        cur.execute(sql)
    for i in range( int( (GAME_WIDTH * GAME_HEIGHT) * configs['env']['food_amount'])):
        cur.execute(configs['sql']['place_food'].replace('!!X', str(randint(0,GAME_WIDTH))).replace('!!Y', str(randint(0,GAME_HEIGHT)) ))


def load_players():
    cur = con.cursor()
    player_count = 1 # 0 = food 
    for g in glob(configs['env']['player_dir'], recursive = True):
        try:
            dot_dna = {}
            with open(g, 'rb') as f:
                dot_dna = json.loads(f.read())

            init_pos = (randint(0,GAME_WIDTH), randint(0,GAME_HEIGHT))
            dot_dna["MAX_X"] = GAME_WIDTH
            dot_dna["MAX_Y"] = GAME_HEIGHT
            dot_dna["flag_x_y"] = init_pos
            dot_dna["init_pos"] = init_pos

            dot_obj_id = get_new_dot(dot_dna, dot_dna['dot_name'])
            cur.execute( configs['sql']['del_initl_pos'].replace('!!X', str( init_pos[0]  )).replace('!!Y', str(init_pos[1])))
            cur.execute( configs['sql']['new_player'].replace("!!id", str( player_count )).replace( "!!name", dot_dna['dot_name']).replace("!!char", 
                    dot_dna['dot_emoji'])  )
            cur.execute( configs['sql']['set_flag'].replace('!!X', str( init_pos[0]  )).replace('!!Y', str(init_pos[1])).replace('!!_name', dot_dna['dot_name']))
            cur.execute( configs['sql']['set_initial_pos'].replace('!!X', str( init_pos[0]  )).replace('!!Y',
                str(init_pos[1])).replace('!!_name', dot_dna['dot_name']).replace("!!UUID", dot_obj_id ))
            player_count += 1
        except Exception as ex:
            print(ex)
            print( traceback.format_exc())
            sys.exit()

def post_event(event, dot_id):
    try:
        target = dot_objects[ dot_id ].dna['onEvents'][event]['target']
    except:
        #dot does not support that event
        return

    name = dot_objects[ dot_id ].dna['dot_name']

    if target == 'self':
        dot_objects[ dot_id ].post_event( event )
    else:
        for dot in dot_objects:
            dot = dot_objects[dot]
            if dot.dna['dot_name'] == name:
                if target == 'some' and random.random() > .9:
                    dot.post_event( event )
            else:
                dot.post_event( event )

def play_game(screen):
    cur = con.cursor()
    while True:
        loop_start = time.time()
        screen.clear()
        for row in cur.execute(configs['sql']['get_all_screen_to_print']):
            screen.print_at(row[2] , row[0], row[1], colour=7)
        screen.refresh()

        dot_keys = list(dot_objects.keys())
        shuffle( dot_keys )
        deleted = []
        for did in dot_keys:
            if did in deleted:
                continue
            dot_objects[did].update(cur)
   
            # This query also limits movment to a distance of 1 
            cur.execute(configs['sql']['get_move_actions'].replace('!!max_x', str(GAME_WIDTH)).replace('!!max_y', str(GAME_HEIGHT) ))
            actions = cur.fetchall()
            for row in actions:
                if row[4] in deleted:
                    continue

                skip_insert = False
                #should be in the yml.. but I miss f :) post_event
                cur.execute(f"select name, is_flag, d_id from main_game_field as a, owner b  where a.owner_id = b.owner_id and X = {row[0]} and Y = {row[1]}")
                collisions = cur.fetchall()
                for c_row in collisions:
                    if row[4] in deleted:
                        continue 
                    elif c_row[0] == 'Food':
                        #spawn
                        n_did = get_new_dot(   dot_objects[ row[4] ].dna, dot_objects[ row[4] ].dna['dot_name'] )
                        
                        cur.execute(f"""insert into main_game_field values ( {dot_objects[ row[4] ].dna['flag_x_y'][0]}, {dot_objects[ row[4] ].dna ['flag_x_y'][1]}, 
                                    (select owner_id from owner where name='{dot_objects[ row[4] ].dna['dot_name']}') , FALSE, '{n_did}' )""")
                        cur.execute(f"delete from main_game_field where X = {row[0]} and Y = {row[1]} and owner_id = (select owner_id from owner where name='Food') ")
                        post_event('on_spawn', row[4])    

                        dot_score_board[dot_objects[ row[4] ].dna['dot_name']]['food'] = dot_score_board[dot_objects[ row[4] ].dna['dot_name']]['food'] + 1
                        dot_score_board[dot_objects[ row[4] ].dna['dot_name']]['alive'] = dot_score_board[dot_objects[ row[4] ].dna['dot_name']]['alive'] + 1
                
                    elif c_row[0] == dot_objects[ row[4] ].dna['dot_name']:
                        #We hit a team member
                        pass
                    elif c_row[1] == 1:
                        #Got a FLAG!!!
                        pass
                    else:
                        #combat 50/50 chance of winning :)
                        if random.choice( [True, False]):
                            skip_insert = True
                            post_event('on_lost_a_battle', row[4])
                            deleted.append( row[4] )
                            cur.execute(f"delete from main_game_field where d_id = '{row[4]}'")
                            dot_score_board[dot_objects[  c_row[2] ].dna['dot_name']]['kills'] = dot_score_board[dot_objects[  c_row[2] ].dna['dot_name']]['kills'] + 1
                            dot_score_board[dot_objects[ row[4] ].dna['dot_name']]['alive'] = dot_score_board[dot_objects[ row[4] ].dna['dot_name']]['alive'] - 1
                            del dot_objects[ row[4] ]
                        else:
                            cur.execute(f"delete from main_game_field where d_id = '{c_row[2]}'");
                            deleted.append( c_row[2] )
                            dot_score_board[dot_objects[ row[4] ].dna['dot_name']]['kills'] = dot_score_board[dot_objects[ row[4] ].dna['dot_name']]['kills'] + 1
                            dot_score_board[dot_objects[  c_row[2] ].dna['dot_name']]['alive'] = dot_score_board[dot_objects[  c_row[2] ].dna['dot_name']]['alive'] - 1
                            post_event('on_kill', row[4])
                            del dot_objects[ c_row[2] ]
                    
                if skip_insert == False:
                    cur.execute(f"""update main_game_field set X = {row[2]} , Y = {row[3]} where d_id = '{did}'""")
            cur.execute("delete from engine_orders")
        if time.time() - loop_start < .5:
            time.sleep(.1)
        con.commit()
        logger.debug(json.dumps(dot_score_board, indent=4))





#Not in a __main__ becuase I don't want this to ever be  imported :)
setup_game()
load_players()
Screen.wrapper(play_game)

