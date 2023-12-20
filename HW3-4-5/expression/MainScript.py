from antlr4 import *
import antlr4.error
from ExpressionLexer import ExpressionLexer
from ExpressionParser import ExpressionParser
from antlr4.error import DefaultErrorStrategy


class CustomErrorStrategy(DefaultErrorStrategy):
    def __init__(self):
        super().__init__()
        self.syntax_errors = 0
        self.error_locations = []

    def recover(self, recognizer, e):
        self.syntax_errors += 1
        line, column = recognizer._input._tokenStartLine, recognizer._input._tokenStartColumn
        self.error_locations.append(f"Line {line}, Position {column}: Syntax error - {e}")
        super().recover(recognizer, e)

    def reportError(self, recognizer, e):
        pass  # Suppress default error messages

    def recoverPhrase(self, recognizer):
        # Implement your custom phrase-level recovery strategy here
        # You can add logic to recover from larger syntax errors
        # For example, skip until a specific token or rule
        pass

    def get_syntax_errors(self):
        return self.syntax_errors

    def get_error_locations(self):
        return '\n'.join(self.error_locations)


# Import your generated lexer and parser (change these imports according to your generated files)

if __name__ == "__main__":
    input_stream = InputStream("3 + 5 * (10 - 2)")
    lexer = ExpressionLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = ExpressionParser(tokens)

    # Set your custom error strategy
    custom_error_strategy = CustomErrorStrategy()
    parser._interp.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION
    parser._errHandler = custom_error_strategy

    # Start parsing from the 'expression' rule
    tree = parser.expression()

    # Check for syntax errors
    if custom_error_strategy.get_syntax_errors() > 0:
        print("Number of syntax errors:", custom_error_strategy.get_syntax_errors())
        print("Error locations:\n", custom_error_strategy.get_error_locations())
    else:
        # Continue processing the parse tree...
        # Optionally, apply phrase-level recovery
        custom_error_strategy.recoverPhrase(parser)
        # Continue processing the parse tree...

