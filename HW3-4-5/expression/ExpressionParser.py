# Generated from C:/Users/black/compiler_design_HW/HW3-4-5/expression/Expression.g4 by ANTLR 4.13.1
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
        4,1,8,35,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        5,1,15,8,1,10,1,12,1,18,9,1,1,2,1,2,1,2,5,2,23,8,2,10,2,12,2,26,
        9,2,1,3,1,3,1,3,1,3,1,3,3,3,33,8,3,1,3,0,0,4,0,2,4,6,0,2,1,0,1,2,
        1,0,3,4,33,0,8,1,0,0,0,2,11,1,0,0,0,4,19,1,0,0,0,6,32,1,0,0,0,8,
        9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,16,3,4,2,0,12,13,7,0,0,0,
        13,15,3,4,2,0,14,12,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,16,17,1,
        0,0,0,17,3,1,0,0,0,18,16,1,0,0,0,19,24,3,6,3,0,20,21,7,1,0,0,21,
        23,3,6,3,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,
        0,25,5,1,0,0,0,26,24,1,0,0,0,27,33,5,7,0,0,28,29,5,5,0,0,29,30,3,
        0,0,0,30,31,5,6,0,0,31,33,1,0,0,0,32,27,1,0,0,0,32,28,1,0,0,0,33,
        7,1,0,0,0,3,16,24,32
    ]

class ExpressionParser ( Parser ):

    grammarFileName = "Expression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_expression = 0
    RULE_additiveExpression = 1
    RULE_multiplicativeExpression = 2
    RULE_primaryExpression = 3

    ruleNames =  [ "expression", "additiveExpression", "multiplicativeExpression", 
                   "primaryExpression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    NUMBER=7
    WS=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(ExpressionParser.AdditiveExpressionContext,0)


        def EOF(self):
            return self.getToken(ExpressionParser.EOF, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ExpressionParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.additiveExpression()
            self.state = 9
            self.match(ExpressionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.MultiplicativeExpressionContext,i)


        def getRuleIndex(self):
            return ExpressionParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = ExpressionParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.multiplicativeExpression()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 12
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 13
                self.multiplicativeExpression()
                self.state = 18
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.PrimaryExpressionContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.PrimaryExpressionContext,i)


        def getRuleIndex(self):
            return ExpressionParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = ExpressionParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.primaryExpression()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 20
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 21
                self.primaryExpression()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ExpressionParser.NUMBER, 0)

        def expression(self):
            return self.getTypedRuleContext(ExpressionParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = ExpressionParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_primaryExpression)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(ExpressionParser.NUMBER)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(ExpressionParser.T__4)
                self.state = 29
                self.expression()
                self.state = 30
                self.match(ExpressionParser.T__5)
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





