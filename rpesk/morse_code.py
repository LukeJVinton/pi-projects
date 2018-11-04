
# 02_blink_twice.py
# From the code for the Electronics Starter Kit for the Raspberry Pi by MonkMakes.com

import RPi.GPIO as GPIO
import time


def word_separation(pin):
    sleep_time = 7
    GPIO.output(pin, False)     # True means that LED turns on
    time.sleep(sleep_time)
    

def pulse(pin, length = "dot"):
    pulse_time = 0
    sleep_time = 1
    if length == "dash":
        pulse_time = 3
    elif length == "dot":
        pulse_time = 1
    elif length == "stop":
        sleep_time = 3
    if length != 'stop':
        GPIO.output(pin, True)     # True means that LED turns on
        time.sleep(pulse_time)                 # delay 0.5 seconds
    GPIO.output(pin, False)     # True means that LED turns on
    time.sleep(sleep_time)


def get_morse_dictionary(letter):
    morse_dict = {'a':['dot','dash','stop'],
                  'b':['dash','dot','dot','dot','stop'],
                  'c':['dash','dot','dash','dot','stop'],
                  'd':['dash','dot','dot','stop'],
                  'e':['dot','stop'],
                  'f':['dot','dot','dash','dot','stop'],
                  'g':['dash','dash','dot','stop'],
                  'h':['dot','dot','dot','dot','stop'],
                  'i':['dot','dot','stop'],
                  'j':['dot','dash','dash','dash','stop'],
                  'k':['dash','dot','dash','stop'],
                  'l':['dot','dash','dot','dot','stop'],
                  'm':['dash','dash','stop'],
                  'n':['dash','dot','stop'],
                  'o':['dash','dash','dash','stop'],
                  'p':['dot','dash','dash','dot','stop'],
                  'q':['dash','dash','dot','dash','stop'],
                  'r':['dot','dash','dot','stop'],
                  's':['dot','dot','dot','stop'],
                  't':['dash','stop'],
                  'u':['dot','dot','dash','stop'],
                  'v':['dot','dot','dot','dash','stop'],
                  'w':['dot','dash','dash','stop'],
                  'x':['dash','dot','dot','dash','stop'],
                  'y':['dash','dot','dash','dash','stop'],
                  'z':['dash','dash','dot','dot','stop'],            
    }
    return morse_dict[letter]


def pulse_letter(letter, pin):
    if letter == ' ':
        word_separation(pin)
    else:
        pulse_list = get_morse_dictionary(letter)
        for beep in pulse_list:
            print(beep)
            pulse(pin, beep)
    


# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
GPIO.setmode(GPIO.BCM)
red_pin1 = 18
GPIO.setup(red_pin1, GPIO.OUT)

try:
    words = input('Enter a word: ')

    for letter in words:
        pulse_letter(letter, red_pin1)

finally:  
    print("Cleaning up")
    GPIO.cleanup()
    
    # You could get rid of the try: finally: code and just have the while loop
    # and its contents. However, the try: finally: construct makes sure that
    # when you CTRL-c the program to end it, all the pins are set back to 
    # being inputs. This helps protect your Pi from accidental shorts-circuits
    # if something metal touches the GPIO pins.
