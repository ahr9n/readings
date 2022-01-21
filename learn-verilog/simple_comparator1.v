// structual modeling
module main
(
    input wire [3:0] x,y,
    output wire z
);
    wire a0,a1,a2,a3;
    xnor (a0,x[0],y[0]);
    xnor (a1,x[1],y[1]);
    xnor (a2,x[2],y[2]);
    xnor (a3,x[3],y[3]);
    and (z,a0,a1,a2,a3);
endmodule