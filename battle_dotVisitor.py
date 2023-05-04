# Generated from battle_dot.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .battle_dotParser import battle_dotParser
else:
    from battle_dotParser import battle_dotParser

# This class defines a complete generic visitor for a parse tree produced by battle_dotParser.

class battle_dotVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by battle_dotParser#start.
    def visitStart(self, ctx:battle_dotParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by battle_dotParser#prog.
    def visitProg(self, ctx:battle_dotParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by battle_dotParser#dot_name.
    def visitDot_name(self, ctx:battle_dotParser.Dot_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by battle_dotParser#dot_emoji.
    def visitDot_emoji(self, ctx:battle_dotParser.Dot_emojiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by battle_dotParser#on_stmt.
    def visitOn_stmt(self, ctx:battle_dotParser.On_stmtContext):
        return self.visitChildren(ctx)



del battle_dotParser