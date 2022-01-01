package simpleinterpreter;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import static simpleinterpreter.TokenType.*;

class Parser {

    private static class ParseError extends RuntimeException {

    }

    private final List<Token> tokens;
    private int current = 0;

    Parser(List<Token> tokens) {
        this.tokens = tokens;
    }

    List<Expr> parse() {
        List<Expr> expressions = new ArrayList<>();
        while (!isAtEnd()) {
            expressions.add(program());
        }

        return expressions;
    }

    private Expr program() {
        try {
            return expression();
        }
        catch (ParseError | IOException error) {
            synchronize();
            return null;
        }
    }

    private Expr expression() throws IOException {
        Expr expr = factor();
/*
           ###############################################################################
                TODO: - Modify the condition of while loop to match PLUS and MINUS. Don't write multiple conditions.
                      - Understand how 'match()' function work to modify it correctly.
                      - Don't add new lines of code, just update the condition.
           ###############################################################################
*/
        while (match(PLUS)) {
            Token operator = previous();
            Expr right = factor();
            expr = new Expr.Binary(expr, operator, right);
        }

        return expr;
    }

    private Expr factor() throws IOException {
        Expr expr = unary();

/*
           ###############################################################################
                TODO: - According to the factor grammar rule: factor → factor ("*" | "/") unary | unary
                      - Write a while loop that parses this rule.
                      - It's a bit similar to the while loop in the 'expression rule' but it parses stars and slashes instead and the (expr.right) is different.
           ###############################################################################
*/

        /* TODO: Add your code below this comment: */



        return expr;
    }

    private Expr unary() throws IOException {
/*
           ###############################################################################
                TODO: - According to the unary grammar rule: unary → ("-") number
                      - Write an if condition to check if there is a minus and parse it correctly.
           ###############################################################################
*/

        /* TODO: Add your code below this comment: */


        return number();
    }

    private Expr number() throws IOException {
        if (match(NUMBER)) {
            return new Expr.Number(previous().literal);
        }
        throw error(peek(), "Expect number.");
    }


    private boolean match(TokenType... types) {
        for (TokenType type : types) {
            if (check(type)) {
                advance();
                return true;
            }
        }

        return false;
    }

    private boolean check(TokenType type) {
        if (isAtEnd()) return false;
        return peek().type == type;
    }

    private Token advance() {
        if (!isAtEnd()){
            current++;
        }
        return previous();
    }

    private boolean isAtEnd() {
        return peek().type == EOF;
    }

    private Token peek() {
        return tokens.get(current);
    }

    private Token previous() {
        return tokens.get(current - 1);
    }

    private ParseError error(Token token, String message) throws IOException {
        SimpleInterpreter.error(token, message);
        return new ParseError();
    }

    private void synchronize() {
        advance();
        while (!isAtEnd()) {
            advance();
        }
    }

}