'''
#1
import time
import RPi.GPIO as GPIO #imports gpio module
GPIO.setmode(GPIO.BCM) #using broadcom mode

GPIO.setup(21, GPIO.OUT) #pin17 is o/p pin
#GPIO.output (21, GPIO.LOW)
a=input("Enter a letter: ")
if a=="a":
    GPIO.output (21, GPIO.HIGH)
    time.sleep(3)
GPIO.output (21, GPIO.LOW)
GPIO.cleanup()


#2
import time
import RPi.GPIO as GPIO #imports GPIO module
GPIO.setmode(GPIO.BCM) #using broadcom mode, enabling use of GPIO pin#

GPIO.setup(21, GPIO.OUT) #pin21 as o/p pin
for i in range (0,5):
    GPIO.output(21,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(21,GPIO.LOW)
    time.sleep(1)
    
GPIO.output(21,GPIO.LOW)
GPIO.cleanup()


#3,#4
import time
import RPi.GPIO as GPIO #imports GPIO module
GPIO.setmode(GPIO.BCM) #setting the pi to operate in broadcom mode

GPIO.setup(21,GPIO.OUT) #21 is the output pin
while True:
    j=0
    for i in range (0,3):
        j+=0.5
        GPIO.output(21,GPIO.HIGH)
        time.sleep(j)
        GPIO.output(21,GPIO.LOW)
        time.sleep(j)
    for i in range (3,0):
        j-=0.5
        GPIO.output(21,GPIO.HIGH)
        time.sleep(j)
        GPIO.output(21,GPIO.LOW)
        time.sleep(j)
GPIO.cleanup()

   
#3 Alternative
import time
import RPi.GPIO as GPIO #imports GPIO module
GPIO.setmode(GPIO.BCM) #setting the pi to operate in broadcom mode

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO.OUT)
j=0.25
k=0.25
loop=1
while True:
    GPIO.output(4,1)
    time.sleep(j)
    GPIO.output(4,0)
    time.sleep(j)
    j=j+k
    print("Waiting time= ", j)
    if j==2 or j==0.25:
        k=-k
GPIO.cleanup()

   
#5
import time
import RPi.GPIO as GPIO #importing GPIO module
GPIO.setmode(GPIO.BCM) #set the pi to Broadcom mode

GPIO.setup([17,21],GPIO.OUT) #pins 17&21 are output pins
GPIO.output([17,21],GPIO.LOW)
while True:
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)
    time.sleep(1)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)
    time.sleep(1)

GPIO.clean()


#6
import time
import RPi.GPIO as GPIO #importing GPIO module
GPIO.setmode(GPIO.BCM) #setting pi to broadcom mode

GPIO.setup([17,27,22,26,21],GPIO.OUT) #setting the pins to output mode

while True:
    GPIO.output(17,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)
    GPIO.output(21,GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(17,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(22,GPIO.LOW)
    GPIO.output(26,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)
    time.sleep(0.5)

GPIO.cleanup()

#6 (improved)
import time
import random
import RPi.GPIO as GPIO #importing the GPIO module
GPIO.setmode (GPIO.BCM) #setting the pi in broadcom mode
GPIO.setup ([17,27,22,26,21], GPIO.OUT) #setting the output pins
GPIO.output ([17,27,22,26,21],GPIO.LOW) #setting it to low in the beginning

def blink():
    GPIO.output([17,27,22,26,21],GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output ([17,27,22,26,21],GPIO.LOW)
    time.sleep(0.5)

while True:
    blink()
    
#7
import time
import RPi.GPIO as GPIO #importing GPIO module
GPIO.setmode(GPIO.BCM) #set pi to Broadcom mode
GPIO.setup([17,27,22,26,21],GPIO.OUT) #setting the pins to output mode
GPIO.output([17,27,22,26,21],GPIO.LOW)


GPIO.output(17,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(27,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(22,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(26,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(21,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(21,GPIO.LOW)
time.sleep(0.5)
GPIO.output(26,GPIO.LOW)
time.sleep(0.5)
GPIO.output(22,GPIO.LOW)
time.sleep(0.5)
GPIO.output(27,GPIO.LOW)
time.sleep(0.5)
GPIO.output(17,GPIO.LOW)
time.sleep(0.5)

GPIO.cleanup()


#7 (improved)
import time
import RPi.GPIO as GPIO #importing GPIO module
GPIO.setmode(GPIO.BCM) #set pi to Broadcom mode
GPIO.setup([17,27,22,26,21],GPIO.OUT) #setting the pins to output mode
GPIO.output([17,27,22,26,21],GPIO.LOW)

def led_seq():
    i=[17,27,22,26,21]
    for a in i:
        GPIO.output(a,GPIO.HIGH)
        time.sleep(0.5)
    i.reverse()
    for b in i:
        GPIO.output(b,GPIO.LOW)
        time.sleep(0.5)

while True:
    led_seq()
GPIO.cleanup()



#8
import time
import random
import RPi.GPIO as GPIO #importing GPIO module
GPIO.setmode (GPIO.BCM) #set pi to broadcom mode
GPIO.setup ([17,27,22,26,21], GPIO.OUT) #setting the output pins
GPIO.output ([17,27,22,26,21], GPIO.LOW)

def random_blink():
    l=[17,27,22,26,21]
    random.shuffle(l)
    for j in l:
        GPIO.output (j,GPIO.HIGH)
        time.sleep(1)
    l.reverse()
    for j in l:
        GPIO.output(j,GPIO.LOW)
        time.sleep(0.5)

while True:
    random_blink()

GPIO.cleanup()


#9
import time
import random
import RPi.GPIO as GPIO #importing the GPIO module
GPIO.setmode (GPIO.BCM) #setting the pi in broadcom mode
GPIO.setup ([17,27,22,26,21], GPIO.OUT) #setting the output pins
GPIO.output ([17,27,22,26,21],GPIO.LOW) #setting it to low in the beginning

def blink():
    GPIO.output([17,27,22,26,21],GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output ([17,27,22,26,21],GPIO.LOW)
    time.sleep(0.5)

def fwd_rev():
    i=[17,27,22,26,21]
    for a in i:
        GPIO.output(a,GPIO.HIGH)
        time.sleep(0.5)
    i.reverse()
    for b in i:
        GPIO.output(b,GPIO.LOW)
        time.sleep(0.5)

def random_blink():
    l=[17,27,22,26,21]
    random.shuffle(l)
    for j in l:
        GPIO.output (j,GPIO.HIGH)
        time.sleep(0.5)
    l.reverse()
    for j in l:
        GPIO.output(j,GPIO.LOW)
        time.sleep(0.5)


while True:
    blink()
    fwd_rev()
    random_blink()
    
GPIO.cleanup()

#sample gpio input program
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.IN)

while True:
    input_state = GPIO.input(19)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
    else:
        print("NOPE!")


'''

#10
import time
import random
import RPi.GPIO as GPIO #importing the GPIO module
GPIO.setmode (GPIO.BCM) #setting the pi in broadcom mode
GPIO.setup ([17,27,22,26,21], GPIO.OUT) #setting the output pins
GPIO.setup(19, GPIO.IN)

GPIO.output ([17,27,22,26,21],GPIO.LOW) #setting it to low in the beginning

def blink():
    GPIO.output([17,27,22,26,21],GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output ([17,27,22,26,21],GPIO.LOW)
    time.sleep(0.5)

def fwd_rev():
    i=[17,27,22,26,21]
    for a in i:
        GPIO.output(a,GPIO.HIGH)
        time.sleep(0.5)
    i.reverse()
    for b in i:
        GPIO.output(b,GPIO.LOW)
        time.sleep(0.5)

def random_blink():
    l=[17,27,22,26,21]
    random.shuffle(l)
    for j in l:
        GPIO.output (j,GPIO.HIGH)
        time.sleep(0.5)
    l.reverse()
    for j in l:
        GPIO.output(j,GPIO.LOW)
        time.sleep(0.5)
print("bug1")
while True:
    if GPIO.input(19):
        print("bug2")
        while True:
            print("bug3")
            blink()
            print("bug4")
            fwd_rev()
            print("bug5")
            random_blink()
            print("bug6")

    else:
        GPIO.output(22,GPIO.HIGH)
GPIO.cleanup()

