# Generated from C:/Users/black/compiler_design_HW/HW3-4-5/expression/Expression.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser

# This class defines a complete generic visitor for a parse tree produced by ExpressionParser.

class ExpressionVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpressionParser#expression.
    def visitExpression(self, ctx:ExpressionParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:ExpressionParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:ExpressionParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressionParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:ExpressionParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)



del ExpressionParser