from antlr4 import FileStream
from emailLexer import emailLexer

def main():
    input_file = "input.txt"
    input_stream = FileStream(input_file)
    lexer = emailLexer(input_stream)

    for token in lexer.getAllTokens():
        if (token.type == 1):
            print("email found :", token.text)


if __name__ == "__main__":
    main()