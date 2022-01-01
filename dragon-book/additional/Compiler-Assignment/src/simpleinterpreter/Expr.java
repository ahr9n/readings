package simpleinterpreter;

abstract class Expr {
    interface Visitor<R> {
        R visitBinaryExpr(Binary expr);
        R visitNumberExpr(Number expr);
        R visitUnaryExpr(Unary expr);
    }

    static class Binary extends Expr {
        Binary(Expr left, Token operator, Expr right) {
            this.left = left;
            this.operator = operator;
            this.right = right;
        }

        @Override
        <R> R accept(Visitor<R> visitor) {
            return visitor.visitBinaryExpr(this);
        }

        final Expr left;
        final Token operator;
        final Expr right;
    }

    static class Unary extends Expr {
        Unary(Token operator, Expr right) {
            this.operator = operator;
            this.right = right;
        }

        @Override
        <R> R accept(Visitor<R> visitor) {
            return visitor.visitUnaryExpr(this);
        }

        final Token operator;
        final Expr right;
    }

    static class Number extends Expr {
        Number(Object value) {
            this.value = value;
        }

        @Override
        <R> R accept(Visitor<R> visitor) {
            return visitor.visitNumberExpr(this);
        }

        final Object value;
    }

    abstract <R> R accept(Visitor<R> visitor);
}