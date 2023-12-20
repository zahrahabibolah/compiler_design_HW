import tree
from antlr4 import *
from ExpressionLexer import ExpressionLexer
from ExpressionParser import ExpressionParser
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.ErrorStrategy import DefaultErrorStrategy
from antlr4.tree import ParseTreeWalker
from ExpressionListener import ExpressionListener

class ExpressionEvaluator(ExpressionListener):
    def __init__(self):
        self.result = None

    def get_result(self):
        return self.result

    # Implement methods from YourExpressionListener to handle specific parse tree events
    # For example:
    def exitNumber(self, ctx):
        self.result = int(ctx.getText())

    def exitAdditiveExpression(self, ctx):
        left = int(ctx.getChild(0).getText())
        right = int(ctx.getChild(2).getText())
        operator = ctx.getChild(1).getText()

        if operator == '+':
            self.result = left + right
        elif operator == '-':
            self.result = left - right

    def exitMultiplicativeExpression(self, ctx):
        left = int(ctx.getChild(0).getText())
        right = int(ctx.getChild(2).getText())
        operator = ctx.getChild(1).getText()

        if operator == '*':
            self.result = left * right
        elif operator == '/':
            self.result = left / right

if __name__ == "__main__":
    # ... (previous code for parsing)

    # No errors, continue processing the parse tree
    evaluator = ExpressionEvaluator()
    walker = ParseTreeWalker()
    walker.walk(evaluator, tree)

    # Print the result
    print("Result:", evaluator.get_result())



class CustomErrorListener(ErrorListener):
    def __init__(self):
        self.syntax_errors = 0
        self.error_locations = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.syntax_errors += 1
        self.error_locations.append(f"Line {line}, Position {column}: {msg}")

    def get_syntax_errors(self):
        return self.syntax_errors

    def get_error_locations(self):
        return '\n'.join(self.error_locations)

class CustomErrorStrategy(DefaultErrorStrategy):
    def recoverPhrase(self, recognizer):
        # Implement your custom phrase-level recovery strategy here
        # This can include skipping until a specific token or rule
        pass

if __name__ == "__main__":
    # Create a lexer and parser
    input_stream = InputStream("3 + 5 * (10 - 2)")
    lexer = ExpressionLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExpressionParser(tokens)

    # Add a custom error listener to the parser
    error_listener = CustomErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Set a custom error strategy
    parser._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION
    parser._errHandler = CustomErrorStrategy()

    # Start parsing from the 'expression' rule
    tree = parser.expression()

    # Check if there were any errors
    if error_listener.get_syntax_errors() > 0:
        print("Number of syntax errors:", error_listener.get_syntax_errors())
        print("Error locations:\n", error_listener.get_error_locations())
    else:
        # No errors, continue processing the parse tree
        evaluator = ExpressionEvaluator()  # Replace with your actual evaluator class
        walker = ParseTreeWalker()
        walker.walk(evaluator, tree)
        print("Result:", evaluator.get_result())
