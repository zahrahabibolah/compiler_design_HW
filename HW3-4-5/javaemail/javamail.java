import org.antlr.v4.runtime.*;

public class EmailIdentifier {
    public static void main(String[] args) throws Exception {
        CharStream input = CharStreams.fromFileName("javamail.java");
        javaemailLexer lexer = new javaemailLexer(input);
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        javaemailParser parser = new javaemailParser(tokens);

        parser.compilationUnit(); // Start parsing from the root rule

        TokenStreamRewriter rewriter = new TokenStreamRewriter(tokens);

        for (Token token : tokens.getTokens()) {
            if (token.getType() == javaemailLexer.EMAIL) {
                System.out.println("Found email address: " + rewriter.getText(token));
            }
        }
    }
}
