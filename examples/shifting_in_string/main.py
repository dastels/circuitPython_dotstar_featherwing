import board
import dotstar_featherwing
import time
import font3

wing = dotstar_featherwing.DotstarFeatherwing(board.D13, board.D11, 0.1)

while True:
	wing.clear()
	wing.shift_in_string(font3.font, "hello adafruit discord!", (0x20, 0x00, 0x20), 0.05)
	time.sleep(2)
