package simpleinterpreter;

enum TokenType {
    // Single-character tokens.
    PLUS, MINUS, SLASH, STAR,

    // Literals.
    NUMBER,

    // End of file token
    EOF
}