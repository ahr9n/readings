module main(
    input a, b, c, d,
    input [3:0] va, vb,
    output w, u, x, y, z,
    output [3:0] vx, vy
);
    assign w = a&b;
    assign u = ~(a|b);
    assign x = c^d;
    assign y = c~^d;
    assign z = (a&b) | (c&d);
    assign vx = va&vb;
    assign vy = va|vb;
endmodule