import pyb
from pyb import Pin, Switch, LED

PIN_D1 = Pin("Y1", Pin.OUT_PP)
PIN_D2 = Pin("Y2", Pin.OUT_PP)
PIN_LAT = Pin("Y4", Pin.OUT_PP)
PIN_OE = Pin("Y3", Pin.OUT_PP)
PIN_A1 = Pin("Y5", Pin.OUT_PP)
PIN_A0 = Pin("Y6", Pin.OUT_PP)
PIN_CLK = Pin("Y7", Pin.OUT_PP)

MAX_STEP = 16
NUM_COLOURS = 3
NUM_BLOCKS = 8

print("Restarted")


def write_bit_to_both(bit):
    PIN_D1.value(bit)
    PIN_D2.value(bit)
    PIN_CLK.value(False)
    PIN_CLK.value(True)


def write_d1(bit):
    PIN_D1.value(bit)
    PIN_CLK.value(False)
    PIN_CLK.value(True)


def write_nowt():
    for i in range(MAX_STEP):
        write_d1(False)


def write_step(step):
    if step > 0:
        for i in range(step):
            write_d1(False)

    write_d1(True)

    if step < MAX_STEP - 1:
        for i in range(step + 1, MAX_STEP):
            write_d1(False)


main_step = 0


def do_write(block):
    current_step = main_step % MAX_STEP
    current_block = main_step // MAX_STEP
    if block != 0 and current_block != block:
        write_nowt()
        write_nowt()
        write_nowt()
        return

    if current_block == block:
        write_step(current_step)
    else:
        write_nowt()

    if block != 0:
        write_nowt()
        write_nowt()
        return

    write_step(current_block)
    write_nowt()

    # block_g = current_block % MAX_STEP
    # block_r = current_block // MAX_STEP
    # write_step(block_g)
    # write_step(block_r)


def write_colour():
    global step

    if step > 0:
        for i in range(step):
            write_bit_to_both(False)

    write_bit_to_both(True)

    if step < MAX_STEP - 1:
        for i in range(step + 1, MAX_STEP):
            write_bit_to_both(False)

    for i in range(16):
        write_bit_to_both(False)

    for i in range(16):
        write_bit_to_both(False)


def write_test():
    # THIS IS WHAT JON RUSSELL DID - EVEN THOUGH IT'S NOT WHAT THE SPEC SAID

    # for i in range(64):
    for i in range(NUM_BLOCKS):
        do_write(i)
        # write_colour()

    PIN_OE.value(True)
    PIN_A0.value(False)
    PIN_A1.value(False)
    PIN_LAT.value(True)
    PIN_LAT.value(False)
    PIN_OE.value(False)


write_test()

led_red = LED(1)
led_green = LED(2)
led_yellow = LED(3)
led_blue = LED(4)


def cycle_step():
    global main_step

    main_step += 1
    if main_step >= MAX_STEP * NUM_BLOCKS:
        main_step = 0
    print(main_step)

    write_test()

    led_yellow.toggle()


sw = Switch()
sw.callback(cycle_step)

t = pyb.Timer(1, freq=100)
t.callback(lambda _: cycle_step())
