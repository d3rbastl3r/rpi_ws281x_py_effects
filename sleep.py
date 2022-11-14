#!/usr/bin/env python3

import time
from rpi_ws281x import PixelStrip, Color

# LED strip configuration:
LED_COUNT = 100       # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def sleepMode(strip, red_max_val, green_max_val, blue_max_val):
    """Light for the night"""
    SLEEP_TIME = 0.005

    for pixel_index in range(strip.numPixels()+1):
        prev_pixel_index = pixel_index - 1 # Index of the pixel we want to fade out

        for brightnes in range(0, 256):
            brightnes_factor = brightnes / 255.0
            red_val = int(red_max_val * brightnes_factor)
            green_val = int(green_max_val * brightnes_factor)
            blue_val = int(blue_max_val * brightnes_factor)

            if pixel_index < strip.numPixels():
                strip.setPixelColor(pixel_index, Color(green_val, red_val, blue_val)) # Fade in pixel
            
            if prev_pixel_index >= 0:
                strip.setPixelColor(prev_pixel_index, Color(green_max_val-green_val, red_max_val-red_val, blue_max_val-blue_val)) # Fade out pixel

            strip.show()
            time.sleep(SLEEP_TIME)

if __name__ == '__main__':
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin() # Intialize the library (must be called once before other functions).
    
    while True:
        print('Light for the night')
        sleepMode(strip, 255, 0, 0)     # Red
        sleepMode(strip, 0, 255, 0)     # Green
        sleepMode(strip, 0, 0, 255)     # Blue
        sleepMode(strip, 255, 162, 57)  # Warm white
        pass