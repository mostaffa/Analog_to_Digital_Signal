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
GPIO.setwarnings(False)
############################################################
# Setting up the chanel, data direction in assemply
GPIO.setup(channel, GPIO.IN)
############################################################
GPIO.setup(7, GPIO.OUT)
print(str(mode) + ' is used.')

# loop through 50 times, on/off for 1 second
for i in range(50):
    GPIO.output(7,True)
    time.sleep(1)
    GPIO.output(7,False)
    time.sleep(1)
GPIO.cleanup()