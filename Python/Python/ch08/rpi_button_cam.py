import RPi.GPIO as GPIO
import picamera
from picamera import Color
import time

def button_capture(channel):
    global capture_on
    with picamera.PiCamera() as camera:
        GPIO.output(led_r_pin, False)
        GPIO.output(led_y_pin, True)
        print("Capturing.....")
        camera.rotation = 180
        camera.resolution = (640, 480)
        camera.start_preview()
        camera.exposure_mode = 'auto'
        camera.annotate_background = Color('black')
        camera.annotate_text = 'Button Capture Testing~~~'
        camera.capture('/home/pi/chiffona/Python/Python/ch08/button_capture.jpg')
        time.sleep(3)
        GPIO.output(led_y_pin, False)
        GPIO.output(led_r_pin, True)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)    
button_pin = 15
led_y_pin = 4
led_r_pin = 17
capture_on = False

GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(led_r_pin, GPIO.OUT)
GPIO.setup(led_y_pin, GPIO.OUT)

GPIO.add_event_detect(button_pin, GPIO.RISING, callback = button_capture, bouncetime = 300)

while 1:
    time.sleep(0.1)