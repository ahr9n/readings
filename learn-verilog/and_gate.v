module main
(
    input wire [1:0] a,
    input wire [1:0] b,
    output wire [1:0]c
);
    assign c = a & b;
endmodule