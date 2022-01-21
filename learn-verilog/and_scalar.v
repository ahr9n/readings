module main
(
    input x,
    input [3:0] d,
    output reg [3:0] q
);
    reg [3:0] tmp;
    integer i;
    always @ (d or x)
        begin
            for(i=0;i<4;i=i+1)
                begin
                    tmp[i] = d[i] & x;
                end
            q = tmp;
        end
endmodule