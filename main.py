from pyb import Pin

PIN_D1 = Pin("Y2", Pin.OUT_PP)
PIN_D2 = Pin("Y1", Pin.OUT_PP)
PIN_LAT = Pin("Y3", Pin.OUT_PP)
PIN_OE = Pin("Y4", Pin.OUT_PP)
PIN_A1 = Pin("Y5", Pin.OUT_PP)
PIN_A0 = Pin("Y6", Pin.OUT_PP)
PIN_CLK = Pin("Y7", Pin.OUT_PP)


def write_bit_to_both(bit):
    PIN_D1.value(bit)
    PIN_D2.value(bit)
    PIN_CLK.value(False)
    PIN_CLK.value(True)


def write_colour():
    # Write blues
    # state = False
    # for i in range(16):
    #     write_bit_to_both(state)
    #     state = not state
    for i in range(7):
        write_bit_to_both(False)
    write_bit_to_both(True)
    for i in range(7):
        write_bit_to_both(False)
    write_bit_to_both(True)

    # Write Greens
    for i in range(16):
        write_bit_to_both(False)
    # Write Reds
    for i in range(16):
        write_bit_to_both(False)


def write_test():
    # THIS IS WHAT JON RUSSELL DID - EVEN THOUGH IT'S NOT WHAT THE SPEC SAID

    for i in range(64):
        write_colour()

    PIN_OE.value(True)
    PIN_A0.value(False)
    PIN_A1.value(False)
    PIN_LAT.value(True)
    PIN_LAT.value(False)
    PIN_OE.value(False)


write_test()
