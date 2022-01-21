// behavioural modeling
module main
(
    input wire [3:0] x,y,
    output wire z
);
    always @(x or y)
        begin
        z = 0;
        if (x == y)
            z = 1;
        end
endmodule