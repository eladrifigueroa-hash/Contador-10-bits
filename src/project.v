/*
 * Copyright (c) 2024 Jason Kaufmann
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_8bitadder (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // Contador de 10 (0 a 9)
  reg [3:0] count;

  always @(posedge clk) begin
    if (!rst_n) begin
      count <= 4'd0;
    end else if (count == 4'd9) begin
      count <= 4'd0;
    end else begin
      count <= count + 4'd1;
    end
  end

  // El conteo sale por los 4 bits bajos; el resto en 0
  assign uo_out = {4'b0000, count};

  // All other output pins must be assigned. If not used, assign to 0.
  assign uio_out = 0;
  assign uio_oe  = 0;

  // List all unused inputs to prevent warnings
  wire _unused = &{ena, ui_in, uio_in, 1'b0};

endmodule
