# Generated from C:/Users/black/compiler_design_HW/HW3-4-5/expression/Expression.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

# This class defines a complete listener for a parse tree produced by ExpressionParser.
class ExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressionParser#expression.
    def enterExpression(self, ctx:ExpressionParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExpressionParser#expression.
    def exitExpression(self, ctx:ExpressionParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExpressionParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:ExpressionParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by ExpressionParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:ExpressionParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by ExpressionParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:ExpressionParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by ExpressionParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:ExpressionParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by ExpressionParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:ExpressionParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by ExpressionParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:ExpressionParser.PrimaryExpressionContext):
        pass



del ExpressionParser