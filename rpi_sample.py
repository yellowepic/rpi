def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(18, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(18, False)
    pwm.ChangeDutyCycle(0)

# Move servo to 90 degrees
set_angle(90)

# Clean up
pwm.stop()
GPIO.cleanup()