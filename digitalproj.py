import board
import time
import terminalio
from adafruit_display_text import bitmap_label

SONICBLUE = 0x290CE4
SNAPCUBEBROWN = 0x964B00
ALFRED = 0xFF0000

while True:
    text = "I'm"
    scale = 5
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=SONICBLUE)
    text_area.x = 20
    text_area.y = 80
    board.DISPLAY.root_group = (text_area)
    time.sleep (0.3)
    text = "going"
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=SNAPCUBEBROWN)
    text_area.x = 20
    text_area.y = 60
    board.DISPLAY.root_group = (text_area)
    time.sleep (0.3)
    text = "to"
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=ALFRED)
    text_area.x = 20
    text_area.y = 60
    board.DISPLAY.root_group = (text_area)
    time.sleep (0.3)
    text = "kill"
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=SNAPCUBEBROWN)
    text_area.x = 20
    text_area.y = 60
    board.DISPLAY.root_group = (text_area)
    time.sleep (0.5)
    text = "you"
    scale = 5
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=SONICBLUE)
    text_area.x = 20
    text_area.y = 60
    board.DISPLAY.root_group = (text_area)
    time.sleep(0.3)
    time.sleep (0.5)
    text = "..."
    scale = 5
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=SNAPCUBEBROWN)
    text_area.x = 20
    text_area.y = 60
    board.DISPLAY.root_group = (text_area)
    time.sleep(1)
    time.sleep (0.5)
    text = "AND"
    scale = 5
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=ALFRED)
    text_area.x = 20
    text_area.y = 60
    board.DISPLAY.root_group = (text_area)
    time.sleep(0.3)
    time.sleep (0.5)
    text = "THEN"
    scale = 5
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=SONICBLUE)
    text_area.x = 20
    text_area.y = 60
    board.DISPLAY.root_group = (text_area)
    time.sleep(0.3)
    time.sleep (0.5)
    text = "KILL"
    scale = 5
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=SNAPCUBEBROWN)
    text_area.x = 20
    text_area.y = 60
    board.DISPLAY.root_group = (text_area)
    time.sleep(0.3)
    time.sleep (0.5)
    text = "YOU"
    scale = 5
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=ALFRED)
    text_area.x = 20
    text_area.y = 60
    board.DISPLAY.root_group = (text_area)
    time.sleep(0.3)
    time.sleep (0.5)
    text = "AGAIN"
    scale = 5
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=SONICBLUE)
    text_area.x = 20
    text_area.y = 60
    board.DISPLAY.root_group = (text_area)
    time.sleep(0.3)
