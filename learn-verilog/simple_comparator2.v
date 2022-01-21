// dataflow modeling
module main
(
    input wire [3:0] x,y,
    output wire z
);
    assign z = &((x ~^y));
endmodule