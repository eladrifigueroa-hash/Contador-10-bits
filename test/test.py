# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, RisingEdge, Timer


@cocotb.test()
async def test_contador_10(dut):
    dut._log.info("Inicio")

    # Reloj de 10 us (100 kHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1
    await Timer(1, unit="us")

    # Tras el reset debe estar en 0
    assert dut.uo_out.value == 0, f"Después del reset se esperaba 0, se obtuvo {dut.uo_out.value}"

    # Verificar la secuencia 0..9 durante 3 vueltas completas
    for i in range(1, 31):
        await RisingEdge(dut.clk)
        await Timer(1, unit="us")
        esperado = i % 10
        assert dut.uo_out.value == esperado, f"Ciclo {i}: se esperaba {esperado}, se obtuvo {dut.uo_out.value}"

    # Reset a mitad de la cuenta
    await ClockCycles(dut.clk, 3)
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 2)
    dut.rst_n.value = 1
    await Timer(1, unit="us")
    assert dut.uo_out.value == 0, "El reset a mitad de cuenta no regresó a 0"

    dut._log.info("Prueba completada")
