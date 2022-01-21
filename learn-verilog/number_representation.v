module main;

reg [31:0] a;
initial
    begin
        a = 15'oz20;
        $display ("Current Value of a = %b", a);
        a = 32'hab_37_56_df;
        $display ("Current Value of a = %b", a);
        a = 12'h12x;
        $display ("Current Value of a = %b", a);
        a = 'h18zx;
        $display ("Current Value of a = %b", a);
        a = 8'd256;
        $display ("Current Value of a = %b", a);
        a = 'ox;
        $display ("Current Value of a = %b", a);
        $finish;
    end
endmodule
