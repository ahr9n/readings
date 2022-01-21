module main
(
    input a, b, c, d,
    output reg  g
);
    reg e,f;
    always @(a or b or c or d)
        begin
            if(a>b)
                e=a;
            else
                e=b;
            if(c>d)
                f=c;
            else
                f=d;
            if(e>f)
                g=e;
            else
                g=f;
        end
endmodule