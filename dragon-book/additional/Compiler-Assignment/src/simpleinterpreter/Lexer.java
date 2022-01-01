package simpleinterpreter;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import static simpleinterpreter.TokenType.*;

class Lexer {
    private final String source;
    private final List<Token> tokens = new ArrayList<>();

    private int start = 0;
    private int current = 0;
    private int line = 1;

    Lexer(String source) {
        this.source = source;
    }

    List<Token> scanTokens() throws IOException {
        while (!isAtEnd()) {
            start = current;
            scanToken();
        }

        tokens.add(new Token(EOF, "", null, line, current, current));
        return tokens;
    }

    private void scanToken() throws IOException {
        char c = advance();
        switch (c) {
/*
           ###############################################################################
                TODO: - Scan "-", "*" and "/" and add them to the list of tokens
                      - You have to use the types defined in 'TokenType' enumeration
                      - Don't write more than three lines of code.
           ###############################################################################
*/

            case '+': addToken(PLUS); break; // Take this line as a guide.
            /* TODO: Add your code below this comment: */


            case ' ': break;
            case '\n': line++; break;

            default:
                if (isDigit(c)) {
                    number();
                }
                else {
                    SimpleInterpreter.error(line, "Unexpected character.");
                }
                break;
        }
    }

    private void number() {
        while (isDigit(peek())) advance();

        if (peek() == '.' && isDigit(peekNext())) {

            advance();

            while (isDigit(peek())) advance();
        }

        addToken(NUMBER, Double.parseDouble(source.substring(start, current)));
    }

    private char peek() {
        if (isAtEnd()) return '\0';
        return source.charAt(current);
    }

    private char peekNext() {
        if (current + 1 >= source.length()) return '\0';
        return source.charAt(current + 1);
    }

    private boolean isDigit(char c) {
        return c >= '0' && c <= '9';
    }


    private boolean isAtEnd() {
        return current >= source.length();
    }


    private char advance() {
        current++;
        return source.charAt(current - 1);
    }

    private void addToken(TokenType type) {
        addToken(type, null);
    }

    private void addToken(TokenType type, Object literal) {
        String text = source.substring(start, current);
        tokens.add(new Token(type, text, literal, line, start, current - 1));
    }
}