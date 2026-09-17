# Arduino CLI
- Arduino CLI is an all-in-one solution that provides Boards/Library Managers, sketch builder, board detection, uploader, and many other tools needed to use any Arduino compatible board and platform from command line or machine interfaces.
- You can use the CLI if you don't want to use the Arduino IDE.

### Update cores and libraries

```bash
# update index and libraries
arduino-cli update

# list outdated core and libraries
arduino-cli outdated

# upgrade core
arduino-cli upgrade
```

### List connected boards

```bash
arduino-cli board list
```

### Creating a new sketch

```bash
arduino-cli sketch new MyFirstSketch
```


### Compiling a sketch

```bash
arduino-cli compile --fqbn arduino:renesas_uno:minima MyAwesomeSketch
```

### Uploading compiled sketch to the board

```bash
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:renesas_uno:minima MyAwesomeSketch
```

### Monitor Serial

```bash
arduino-cli monitor -p /dev/ttyACM0
```

## References
- [Arduino CLI](https://docs.arduino.cc/arduino-cli/)