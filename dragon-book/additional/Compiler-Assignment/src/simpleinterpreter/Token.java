package simpleinterpreter;

class Token {
    final TokenType type;
    final String lexeme;
    final Object literal;
    final int line;
    final int start;
    final int end;

    Token(TokenType type, String lexeme, Object literal, int line, int start, int end) {
        this.type = type;
        this.lexeme = lexeme;
        this.literal = literal;
        this.line = line;
        this.start = start;
        this.end = end;
    }

    public String toString() {
        return "Token Type: " + type + ", Lexeme: " + lexeme + ", Literal Value: " + literal + " at Line: " + line + " [" + start + ", " + end + "]";
    }
}