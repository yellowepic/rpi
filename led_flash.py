import RPi.GPIO as GPIO
import time

# Set up the GPIO pin numbering mode
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for the LED
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("LED is ON")
        time.sleep(1)  # Wait for 1 second

        # Turn the LED off
        GPIO.output(LED_PIN, GPIO.LOW)
        print("LED is OFF")
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Clean up the GPIO pins on exit
    GPIO.cleanup()
    print("Program exited cleanly")