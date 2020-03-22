#import the GPIO and time package
try:
    import RPi.GPIO as GPIO
    print('Importing RPI.GPIO Done...')
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
import time
############################################################
GPIO.setmode(GPIO.BOARD)
# GPIO.setmode(GPIO.BCM) for BCM Board
############################################################
mode = GPIO.getmode()# returns which board using in Raspberry
# -1 if GPIO.setmode() is not set
# 11 if GPIO.setmode(GPIO.BCM) is active
# 10 if GPIO.setmode(GPIO.BOARD) is active
############################################################
# enable/ disable warning
GPIO.setwarnings(True)
############################################################
# Setting up the chanel, data direction in assemply
GPIO.setup(21, GPIO.OUT)
GPIO.setup(40,GPIO.IN, pull_up_down=GPIO.PUD_UP)
############################################################
timer = 0.1
print(str(mode) + ' is used.')
# GPIO.wait_for_edge(40, GPIO.RISING)
############################################################
# chan_list = [11,12]                             # also works with tuples
# GPIO.output(chan_list, GPIO.LOW)                # sets all to GPIO.LOW
# GPIO.output(chan_list, (GPIO.HIGH, GPIO.LOW))   # sets first HIGH and second LOW
############################################################
print(GPIO.RPI_REVISION)
# loop through 50 times, on/off for 1 second
while True:
    #block execution of your program until an edge is detected
    GPIO.wait_for_edge(40, GPIO.RISING)
    # print(GPIO.PUD_DOWN)
    # if GPIO.input(40):
    #     print('Input was HIGH')
    # else:
    #     print('Input was LOW')
    GPIO.output(21,True)
    time.sleep(0.11)
    GPIO.output(21,False)
    time.sleep(0.23)
    GPIO.output(21, True)
    time.sleep(0.11)
    GPIO.output(21, False)
    time.sleep(0.55)
    # if not GPIO.input(40):
    #     break
GPIO.cleanup()