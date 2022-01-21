`timescale 1ns / 1ps
module main;
    // Inputs
    reg a;
    reg b;
    reg c;
    reg d;
    // Outputs
    wire g;
    // Instantiate the Unit Under Test (UUT)
    comparator uut (
        .a(a), .b(b), .c(c), .d(d), .g(g)
    );
    initial
        begin
            a = 0;
            b = 0;
            c = 0;
            d = 0;
        end
    always
        begin
            #50 a = ~a;
        end
    always
        begin
            #100 b = ~b;
        end
    always
        begin
            #200 c = ~c;
        end
    always
        begin
            #400 d = ~d;
        end
endmodule