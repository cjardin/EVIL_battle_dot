from battle_dotVisitor import battle_dotVisitor
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .battle_dotParser import battle_dotParser
else:
    from battle_dotParser import battle_dotParser

import json

class dot_generator(battle_dotVisitor):

    def __init__(self):
        self.prog = {"onEvents": {} }
        super(battle_dotVisitor, self).__init__()

    def __del__(self):
        with open(f"compiled_players/{self.prog['dot_name']}.json", 'wb') as f:
            f.write( json.dumps(self.prog, indent=4, ensure_ascii=False).encode('utf8') )

        return

    def visitStart(self, ctx:battle_dotParser.StartContext):
        return super().visitStart(ctx)


    def visitProg(self, ctx:battle_dotParser.ProgContext):
        return super().visitProg(ctx)


    def visitDot_name(self, ctx:battle_dotParser.Dot_nameContext):
        self.prog['dot_name'] = str(ctx.NAME_ID())
        
        return super().visitDot_name(ctx)


    def visitDot_emoji(self, ctx:battle_dotParser.Dot_emojiContext):
        f = str(ctx.EMOJI())
        self.prog['dot_emoji'] = f
        return super().visitDot_emoji(ctx)


    def visitOn_stmt(self, ctx:battle_dotParser.On_stmtContext):

        self.prog['onEvents'][str(ctx.ON_STMT_NAMES())] = {}

        self.prog['onEvents'][str(ctx.ON_STMT_NAMES())]['actor'] = str(ctx.BEHAVIOR_NAMES())

        self.prog['onEvents'][str(ctx.ON_STMT_NAMES())]['params'] = []
        i = 0
        while True:
            v = ctx.VALUE(i) 
            if v == None:
                break
            self.prog['onEvents'][str(ctx.ON_STMT_NAMES())]['params'].append(float( str(v) ))
            i += 1

        if ctx.TARGETS() != None:
            self.prog['onEvents'][str(ctx.ON_STMT_NAMES())]['target'] = str(ctx.TARGETS())

        return super().visitOn_stmt(ctx)



del battle_dotParser
