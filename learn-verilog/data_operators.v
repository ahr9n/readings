module main;
    initial
        begin
            //Reduction
            $display("&4'b0101= %b", &4'b0101);
            // relationship operators
            $display ("5'b1001x ===  5'b1001x= %b", (5'b1001x === 5'b1001x));
            $display ("1'bz  <=  10 = %b", (1'bz  <= 10));
            // Bit Wise
            $display ("~4'b10xz= %b", (~4'b10xz));
            // Logical operators
            $display ("1'b1 || 1'b0 = %b", (1'b1 || 1'b0));
            // arithmetic operators
            $display ("2**4 = %d", 2**4);
        end
endmodule