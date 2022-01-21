`timescale 1ns / 1ps
module main;
    // Inputs
    reg d;
    reg clk;
    reg rst;
    // Outputs
    wire q;
    // Instantiate the Unit Under Test (UUT)
    d_flip_flop uut
    (
        .d(d),.clk(clk),.rst(rst),.q(q)
    );
    // Initialize Inputs
    initial
        begin
            d = 0;
            clk = 0;
            rst = 0;
        end
    always #50 clk = ~clk;
    always #50 rst = 0;
    always #100 d = ~d;
endmodule