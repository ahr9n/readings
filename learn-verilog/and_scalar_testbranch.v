`timescale 1ns / 1ps
module and_tb;
    // Inputs
    reg x;
    reg [3:0] d;
    // Outputs
    wire [3:0] q;
    // Instantiate the Unit Under Test (UUT)
    and_scalar uut
    (
        .x(x), .d(d), .q(q)
    );
    initial
        begin
            d = 0;
            forever begin #50 d=4'b1010; end
        end
    initial
        begin
            x = 0;
            repeat(8)  begin  #50 x=~x; end
        end
endmodule