from machine import Pin
from machine import SPI

from drivers.st7789 import ST7789_SPI

def st7789():
    spi = SPI(0)
    # Mode 3, maximum clock speed!
    spi.init(polarity=1, phase=1, baudrate=8000000)
    
    # Configure the display
    cs = Pin("SPI_SS2", Pin.OUT)
    dc = Pin("P18", Pin.OUT)
    rst = Pin("P26", Pin.OUT)
    tft = ST7789_SPI(240, 240, spi, cs=cs, dc=dc, res=rst)

    # Bring up the backlight
    bl = Pin("P22", Pin.OUT)
    bl.off() # active low
    return tft