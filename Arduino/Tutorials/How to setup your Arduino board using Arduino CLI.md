# How to setup your Arduino board using Arduino CLI

Requirements
- Arduino CLI
- Arduino board

## Steps

1. Update core index
    
    ```
    arduino-cli core update-index
    ```

2. Connect your board to your computer using a USB cable that can transfer data. USB cable for chargers won't recognize your board.

3. Once connected, run this board command to check if your computer will see your board connected

    ```
    arduino-cli board list
    ```

    Expected output

    ```
    Port         Protocol Type              Board Name            FQBN                       Core
    /dev/ttyACM0 serial   Serial Port (USB) Arduino UNO R4 Minima arduino:renesas_uno:minima arduino:renesas_uno
    ```

    If no boards found, you need search for the Core in the Arduino package index:

    ```
    arduino-cli core search or
    arduino-cli board search
    ```

4. After identifying the the core for your board, install it

    ```
    arduino-cli core install <core name>
    ```

5. Verify installed core

    ```
    arduino-cli core list
    ```

    Expected output

    ```
    arduino:avr         1.8.8     1.8.8  Arduino AVR Boards
    arduino:renesas_uno 1.6.0     1.6.0  Arduino UNO R4 Boards
    ```