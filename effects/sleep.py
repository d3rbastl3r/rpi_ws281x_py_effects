#!/usr/bin/env python3

import time

import click

from rpi_ws281x import PixelStrip, Color

# LED strip default configuration:
#LED_COUNT = 50       # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

@click.command()
@click.option('-l', '--leds', type=int, default=50, show_default=True, help='Amount of LEDs in the string')
@click.option('-s', '--speed', type=float, default=1.0, show_default=True, help='Speed of the effect')
@click.option('-c', '--color', type=str, default='FF0000', show_default=True, help='RGB Value for the effect. You need to provide this value as a hexadecimal.')
def main(leds: int, speed: float, color: str):
    '''
    This is a sleep effect which provide a light for the night
    '''
    if not color.startswith('0x'):
        color = '0x' + color
        
    print(f'Sleep effect started with following parameter: leds={leds}, speed={speed}, color={color}')
    color_dict = parseColorString(color)
    
    strip = PixelStrip(leds, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin() # Intialize the library (must be called once before other functions).
    
    runEffect(strip, speed, color_dict['red'], color_dict['green'], color_dict['blue']);
    pass

def parseColorString(color: str):
    '''
    Parse the color given as string to single RGB colors as int values and return the dictionary with
    parsed values
    '''
    color_int_val = int(color, base=16)
    red_mask = 0xFF0000
    green_mask = 0x00FF00
    blue_mask = 0x0000FF
    
    return {
        'red': (color_int_val & red_mask)>>16,
        'green': (color_int_val & green_mask)>>8,
        'blue': (color_int_val & blue_mask)>>0
    }

def runEffect(strip, speed, red_max_val, green_max_val, blue_max_val):
    SLEEP_TIME = 0.005 * speed

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
    pass

if __name__ == "__main__":
    main()