# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Example for TFlipFlop

# <codecell>

from __future__ import print_function
from BinPy.Sequential.sequential import TFlipFlop
from BinPy.tools.clock import Clock
from BinPy.Gates import Connector
from BinPy.tools.oscilloscope import Oscilloscope

# <codecell>

toggle = Connector(1)

p = Connector(0)
q = Connector(1)

# <codecell>

# Initialize the clock
clock = Clock(1, 4)
clock.start()
# A clock of 4 hertz frequency
clk_conn = clock.A

enable = Connector(1)

# <codecell>

# Initialize the T-FlipFlop
tff = TFlipFlop(toggle, enable, clk_conn, a=p, b=q)

# To connect different set of connectors use :
# tff.setInputs(conn1,enab,clk)
# To connect different outputs use:
tff.setOutputs(A=p, B=q)

# <codecell>

# Initialize the oscilloscope
o = Oscilloscope((clk_conn, 'CLK'), (toggle, 'TOGGLE'), (
    p, 'OUT'), (q, 'OUT!'), (enable, 'ENABLE'))
o.start()
o.setScale(0.01)  # Set scale by trial and error.
o.setWidth(100)
o.unhold()

# <codecell>

print ("Toggle is 1")
toggle.state = 1
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        tff.trigger()
        break
print (tff.state())

# Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        tff.trigger()
        break

# <codecell>

print ("Toggle is 1")
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        tff.trigger()
        break
print (tff.state())

# Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        tff.trigger()
        break

# <codecell>

print ("Toggle is 1")
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        tff.trigger()
        break
print (tff.state())

# Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        tff.trigger()
        break

# <codecell>

print ("Toggle is 0")
toggle.state = 0
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        tff.trigger()
        break
print (tff.state())

# Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        tff.trigger()
        break

# <codecell>

print ("Toggle is 0")
while True:
    if clk_conn.state == 0:
        # Falling edge will trigger the FF
        tff.trigger()
        break
print (tff.state())

# Sending a positive edge to ff
while True:
    if clk_conn.state == 1:
        # Falling edge will trigger the FF
        tff.trigger()
        break

# <codecell>

# Display the oscilloscope
o.display()

# <codecell>

# Kill the oscilloscope and clock threads after use
o.kill()
clock.kill()
