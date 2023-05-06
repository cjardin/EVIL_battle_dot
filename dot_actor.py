import random
import logging
import importlib

logger = logging.getLogger()

class dot_actor:
    def __init__(self, dna, my_id):
        self.dna = dna
        self.id = my_id
        self.new_behavior('on_start')

    def new_behavior(self, event_name):
        try:
            self.behavior = importlib.import_module( f"behaviors.{self.dna['onEvents'][event_name]['actor']}")
            self.behavior_state = {}
        except:
            #behavior did not support event
            pass

    def update(self, db_cursor):
        #get all my dots
        self.behavior.update(self.dna, self.id,  self.behavior_state, db_cursor)

    def post_event(self, event_name):
        self.new_behavior(event_name)

