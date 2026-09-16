# Arduino CLI
- Arduino CLI is an all-in-one solution that provides Boards/Library Managers, sketch builder, board detection, uploader, and many other tools needed to use any Arduino compatible board and platform from command line or machine interfaces.
- You can use the CLI if you don't want to use the Arduino IDE

### Creating a new sketch

```
arduino-cli sketch new MyFirstSketch
```


### Compiling a sketch

```
arduino-cli compile --fqbn arduino:renesas_uno:minima MyAwesomeSketch
```

### Uploading compiled sketch to the board

```
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:renesas_uno:minima MyAwesomeSketch
```

## References
- [Arduino CLI](https://docs.arduino.cc/arduino-cli/)