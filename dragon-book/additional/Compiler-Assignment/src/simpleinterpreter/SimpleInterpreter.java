package simpleinterpreter;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;

public class SimpleInterpreter {
    static boolean hadError = false;

    static void error(Token token, String message) throws IOException {
        if (token.type == TokenType.EOF) {
            report(token.line, " at end", message);
        } else {
            report(token.line, " at '" + token.lexeme + "'", message);
        }
    }

    static void error(int line, String message) throws IOException {
        report(line, "", message);
    }

    private static void report(int line, String where, String message) throws IOException {
        String output = "[line " + line + "] Error" + where + ": " + message;
        System.err.println(output);
        hadError = true;
    }

    static void runtimeError(RuntimeError error) throws IOException {
        String output = error.getMessage() + "\n[line " + error.token.line + "]";
        System.err.println(output);
    }

    private static void run(String source) throws IOException {
        Lexer scanner = new Lexer(source);

        System.out.println("Lexical Analysis:");
        List<Token> tokens = scanner.scanTokens();

        for(Token token : tokens){
            System.out.println(token);
        }

        Parser parser = new Parser(tokens);
        System.out.println("Parsing:");
        List<Expr> expressions = parser.parse();

        if (hadError) return;

        for(Expr ex : expressions) {
            System.out.println(new AstPrinter().print(ex));
        }

        Interpreter interpreter = new Interpreter();

        System.out.println("Interpreting:");
        interpreter.interpret(expressions);
    }

    private static void runPrompt() throws IOException {
        InputStreamReader input = new InputStreamReader(System.in);
        BufferedReader reader = new BufferedReader(input);

        for (;;) {
            System.out.print("> ");
            String line = reader.readLine();
            if (line == null) {
                break;
            }
            run(line);
            if (hadError) {
                System.exit(65);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        runPrompt();
    }

}
