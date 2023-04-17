from battle_dotVisitor import battle_dotVisitor
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .battle_dotParser import battle_dotParser
else:
    from battle_dotParser import battle_dotParser

class dot_generator(battle_dotVisitor):

    def __init__(self):
        super(battle_dotVisitor, self).__init__()

    def visitStart(self, ctx:battle_dotParser.StartContext):
        print(1)
        return super().visitStart(ctx)


    def visitProg(self, ctx:battle_dotParser.ProgContext):
        print(2)
        return super().visitProg(ctx)


    def visitDot_name(self, ctx:battle_dotParser.Dot_nameContext):
        print(3)
        return super().visitDot_name(ctx)


    def visitDot_emoji(self, ctx:battle_dotParser.Dot_emojiContext):
        print(4)
        return super().visitDot_emoji(ctx)


    def visitOn_stmt(self, ctx:battle_dotParser.On_stmtContext):
        print(5)
        return super().visitOn_stmt(ctx)



del battle_dotParser
