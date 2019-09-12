#!/usr/bin/env python3
import blinkt, sys

if len(sys.argv) < 2:
	color = "clear"
else:
	color = sys.argv[1]

#clear lights
blinkt.set_clear_on_exit(False)
blinkt.set_brightness(0.1)
blinkt.set_all(0, 0, 0)
blinkt.show()

if color == "red":
	blinkt.set_clear_on_exit(False)
	blinkt.set_brightness(0.5)
	blinkt.set_all(255, 0, 0)
elif color == "green":
	blinkt.set_clear_on_exit(False)
	blinkt.set_brightness(0.5)
	blinkt.set_all(9, 255, 0)
elif color == "yellow":
	blinkt.set_clear_on_exit(False)
	blinkt.set_brightness(0.5)
	blinkt.set_all(255, 63, 0)
elif color == "blue":
	blinkt.set_clear_on_exit(False)
	blinkt.set_brightness(0.5)
	blinkt.set_all(0, 15, 255)
else:
	blinkt.set_clear_on_exit(True)
#	blinkt.set_brightness(0.1)
#	blinkt.set_all(0, 0, 0)

blinkt.show()
