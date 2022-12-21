# WS281x Project using "rpi_ws281x" library

# RPi Setup

* There is a neet to configure the Raspberry Pi to be able send data to the ws281x LEDs via PWM. As long as all the required steps are not discovered please use following links to perform the setup:
  * https://tutorials-raspberrypi.de/raspberry-pi-ws2812-ws2811b-rgb-led-streifen-steuern/
  * https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black
  * https://github.com/jgarff/rpi_ws281x
  * https://github.com/rpi-ws281x/rpi-ws281x-python

# Execution (how to)

* If any python dependencies are missing, install all dependencies by executin following command:
    ```bash
    # Because we need to run scripts as sudo, we also need to install libraries for sudo user
    sudo python3 -m pip install -r requirements.txt
    ```
