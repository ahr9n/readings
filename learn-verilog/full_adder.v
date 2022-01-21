module main
(
    input a,b,c,
    output sum,carry
);
    wire s1,c1,c2;
    half_adder ha1
    (
    .a(a),.b(b),.sum(s1),.carry(c1)
    );
    half_adder ha2
    (
    .a(c),.b(s1),.sum(sum),.carry(c2)
    );
    assign carry = c1|c2;
endmodule