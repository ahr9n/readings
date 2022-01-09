import java.io.*;

class Parser {
    static int lookahead;

    public Parser() throws IOException {
        lookahead = System.in.read();
    }

    public void stmt() throws Exception {
        match('0');
        if (lookahead == '1') {
            match('1');
        } else {
            stmt(); match('1');
        }
    }

    void match(int t) throws IOException {
        if (lookahead == t) {
            lookahead = System.in.read();
        } else {
            throw new Error("syntax error");
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Parser parse = new Parser();
        try {
            parse.stmt();
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}
