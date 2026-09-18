BOARD ?= arduino:renesas_uno:minima
PORT ?= /dev/ttyACM0
SKETCH ?= .

.PHONY: all build upload monitor boards clean

all: build upload

build:
	arduino-cli compile --fqbn $(BOARD) $(SKETCH)

upload:
	arduino-cli upload --fqbn $(BOARD) --port $(PORT) $(SKETCH)

monitor:
	arduino-cli monitor --port $(PORT)

boards:
	arduino-cli board list

# Clean build files system-wide
clean:
	arduino-cli cache clean