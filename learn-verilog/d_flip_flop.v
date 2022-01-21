module main
(
    input wire d,clk,rst,
    output reg q
);
    always @ (posedge clk)
        begin
            if (rst == 1'b1)
                q <= 0;
            else
                q <= d;
        end
endmodule