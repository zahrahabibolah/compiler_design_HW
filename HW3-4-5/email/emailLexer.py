# Generated from C:/Users/black/compiler_design_HW/HW3-4-5/email.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,2,32,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,11,8,0,11,
        0,12,0,12,1,1,4,1,16,8,1,11,1,12,1,17,1,2,1,2,1,2,1,2,1,2,1,2,1,
        3,4,3,27,8,3,11,3,12,3,28,1,3,1,3,0,0,4,1,0,3,0,5,1,7,2,1,0,3,7,
        0,37,37,43,43,45,46,48,57,65,90,95,95,97,122,4,0,45,46,48,57,65,
        90,97,122,3,0,9,10,13,13,32,32,32,0,5,1,0,0,0,0,7,1,0,0,0,1,10,1,
        0,0,0,3,15,1,0,0,0,5,19,1,0,0,0,7,26,1,0,0,0,9,11,7,0,0,0,10,9,1,
        0,0,0,11,12,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,2,1,0,0,0,14,
        16,7,1,0,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,
        0,18,4,1,0,0,0,19,20,3,1,0,0,20,21,5,64,0,0,21,22,3,3,1,0,22,23,
        5,46,0,0,23,24,3,3,1,0,24,6,1,0,0,0,25,27,7,2,0,0,26,25,1,0,0,0,
        27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,30,1,0,0,0,30,31,6,
        3,0,0,31,8,1,0,0,0,4,0,12,17,28,1,6,0,0
    ]

class emailLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EMAIL = 1
    WS = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "EMAIL", "WS" ]

    ruleNames = [ "LOCAL_SUBPART", "DOMAIN_SUBPART", "EMAIL", "WS" ]

    grammarFileName = "email.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


