# Generated from battle_dot.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,53,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,3,0,13,
        8,0,1,1,1,1,1,1,4,1,18,8,1,11,1,12,1,19,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,39,8,4,10,4,12,4,
        42,9,4,3,4,44,8,4,1,4,1,4,1,4,3,4,49,8,4,1,4,1,4,1,4,0,0,5,0,2,4,
        6,8,0,0,52,0,12,1,0,0,0,2,14,1,0,0,0,4,21,1,0,0,0,6,26,1,0,0,0,8,
        31,1,0,0,0,10,13,3,2,1,0,11,13,1,0,0,0,12,10,1,0,0,0,12,11,1,0,0,
        0,13,1,1,0,0,0,14,15,3,4,2,0,15,17,3,6,3,0,16,18,3,8,4,0,17,16,1,
        0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,3,1,0,0,0,21,
        22,5,1,0,0,22,23,5,2,0,0,23,24,5,12,0,0,24,25,5,3,0,0,25,5,1,0,0,
        0,26,27,5,4,0,0,27,28,5,2,0,0,28,29,5,13,0,0,29,30,5,3,0,0,30,7,
        1,0,0,0,31,32,5,9,0,0,32,33,5,2,0,0,33,34,5,10,0,0,34,43,5,5,0,0,
        35,40,5,14,0,0,36,37,5,6,0,0,37,39,5,14,0,0,38,36,1,0,0,0,39,42,
        1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,
        43,35,1,0,0,0,43,44,1,0,0,0,44,45,1,0,0,0,45,48,5,7,0,0,46,47,5,
        8,0,0,47,49,5,11,0,0,48,46,1,0,0,0,48,49,1,0,0,0,49,50,1,0,0,0,50,
        51,5,3,0,0,51,9,1,0,0,0,5,12,19,40,43,48
    ]

class battle_dotParser ( Parser ):

    grammarFileName = "battle_dot.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'dot_name'", "':'", "';'", "'dot_emoji'", 
                     "'('", "','", "')'", "'->'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ON_STMT_NAMES", "BEHAVIOR_NAMES", "TARGETS", 
                      "NAME_ID", "EMOJI", "VALUE", "WS" ]

    RULE_start = 0
    RULE_prog = 1
    RULE_dot_name = 2
    RULE_dot_emoji = 3
    RULE_on_stmt = 4

    ruleNames =  [ "start", "prog", "dot_name", "dot_emoji", "on_stmt" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ON_STMT_NAMES=9
    BEHAVIOR_NAMES=10
    TARGETS=11
    NAME_ID=12
    EMOJI=13
    VALUE=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prog(self):
            return self.getTypedRuleContext(battle_dotParser.ProgContext,0)


        def getRuleIndex(self):
            return battle_dotParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = battle_dotParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.prog()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dot_name(self):
            return self.getTypedRuleContext(battle_dotParser.Dot_nameContext,0)


        def dot_emoji(self):
            return self.getTypedRuleContext(battle_dotParser.Dot_emojiContext,0)


        def on_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(battle_dotParser.On_stmtContext)
            else:
                return self.getTypedRuleContext(battle_dotParser.On_stmtContext,i)


        def getRuleIndex(self):
            return battle_dotParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = battle_dotParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.dot_name()
            self.state = 15
            self.dot_emoji()
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.on_stmt()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dot_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME_ID(self):
            return self.getToken(battle_dotParser.NAME_ID, 0)

        def getRuleIndex(self):
            return battle_dotParser.RULE_dot_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDot_name" ):
                listener.enterDot_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDot_name" ):
                listener.exitDot_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDot_name" ):
                return visitor.visitDot_name(self)
            else:
                return visitor.visitChildren(self)




    def dot_name(self):

        localctx = battle_dotParser.Dot_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_dot_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(battle_dotParser.T__0)
            self.state = 22
            self.match(battle_dotParser.T__1)
            self.state = 23
            self.match(battle_dotParser.NAME_ID)
            self.state = 24
            self.match(battle_dotParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dot_emojiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMOJI(self):
            return self.getToken(battle_dotParser.EMOJI, 0)

        def getRuleIndex(self):
            return battle_dotParser.RULE_dot_emoji

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDot_emoji" ):
                listener.enterDot_emoji(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDot_emoji" ):
                listener.exitDot_emoji(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDot_emoji" ):
                return visitor.visitDot_emoji(self)
            else:
                return visitor.visitChildren(self)




    def dot_emoji(self):

        localctx = battle_dotParser.Dot_emojiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_dot_emoji)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(battle_dotParser.T__3)
            self.state = 27
            self.match(battle_dotParser.T__1)
            self.state = 28
            self.match(battle_dotParser.EMOJI)
            self.state = 29
            self.match(battle_dotParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class On_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ON_STMT_NAMES(self):
            return self.getToken(battle_dotParser.ON_STMT_NAMES, 0)

        def BEHAVIOR_NAMES(self):
            return self.getToken(battle_dotParser.BEHAVIOR_NAMES, 0)

        def VALUE(self, i:int=None):
            if i is None:
                return self.getTokens(battle_dotParser.VALUE)
            else:
                return self.getToken(battle_dotParser.VALUE, i)

        def TARGETS(self):
            return self.getToken(battle_dotParser.TARGETS, 0)

        def getRuleIndex(self):
            return battle_dotParser.RULE_on_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOn_stmt" ):
                listener.enterOn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOn_stmt" ):
                listener.exitOn_stmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOn_stmt" ):
                return visitor.visitOn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def on_stmt(self):

        localctx = battle_dotParser.On_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_on_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(battle_dotParser.ON_STMT_NAMES)
            self.state = 32
            self.match(battle_dotParser.T__1)
            self.state = 33
            self.match(battle_dotParser.BEHAVIOR_NAMES)
            self.state = 34
            self.match(battle_dotParser.T__4)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 35
                self.match(battle_dotParser.VALUE)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 36
                    self.match(battle_dotParser.T__5)
                    self.state = 37
                    self.match(battle_dotParser.VALUE)
                    self.state = 42
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 45
            self.match(battle_dotParser.T__6)
            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 46
                self.match(battle_dotParser.T__7)
                self.state = 47
                self.match(battle_dotParser.TARGETS)


            self.state = 50
            self.match(battle_dotParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





