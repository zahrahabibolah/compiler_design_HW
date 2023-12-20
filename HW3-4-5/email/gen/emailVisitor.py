# Generated from C:/Users/black/compiler_design_HW/HW3-4-5/email.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .emailParser import emailParser
else:
    from emailParser import emailParser

# This class defines a complete generic visitor for a parse tree produced by emailParser.

class emailVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by emailParser#email.
    def visitEmail(self, ctx:emailParser.EmailContext):
        return self.visitChildren(ctx)



del emailParser