import BlynkLib
from sense_hat import SenseHat
from time import sleep
#importing subprocess to call the aplay method for bluetooth speaker
from subprocess import call


"""preliminary setup of bluetooth speaker done as follows:
   bluetoothctl
   scan on (discover Device addresses of blueooth devices)
   pair D4:F5:47:D8:96:D8 (Device address of bluetooth speaker)
   trust D4:F5:47:D8:96:D8 (sets speaker as trusted device)
   connect D4:F5:47:D8:96:D8 (connects to bluetooth speaker)
   quit (to leave bluetoothctl)"""

BLYNK_AUTH = 'bW41ErtD_gpFZjnjTrKxVYdFjIazxoZG'
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

#initialise SenseHat and camera
sense = SenseHat()
sense.clear()

#declare variables
b = (0,0,255)
r = (255,0,0)
o = (255,128,0)
yo = (255,200,0)
ye = (255,255,0)
bl = (0,0,0)
flame = [bl,r,bl,bl,bl,r,bl,bl,
         bl,r,r,bl,r,r,bl,bl,
         bl,bl,bl,r,r,yo,r,bl,
         bl,bl,r,r,o,yo,o,bl,
         bl,bl,r,o,ye,ye,o,r,
         bl,bl,r,yo,ye,o,r,bl,
         bl,bl,bl,r,yo,r,bl,bl,
         bl,bl,bl,bl,r,bl,bl,bl]
ice = [bl,bl,bl,bl,bl,bl,bl,bl,
       b,bl,bl,b,bl,bl,b,bl,
       bl,bl,b,b,b,bl,bl,bl,
       bl,b,bl,b,bl,b,bl,bl,
       b,b,b,b,b,b,b,bl,
       bl,b,bl,b,bl,b,bl,bl,
       bl,bl,b,b,b,bl,bl,bl,
       b,bl,bl,b,bl,bl,b,bl]

# infinite loop that waits for event
while True:
    blynk.run()
    temp = (sense.temperature -7)
    maxTemp = 22
    minTemp = 17
#if statement for max. temperature event
    if temp >= maxTemp:
#write the temperature reading to the console
     blynk.virtual_write(1, round((sense.temperature -7),1))
#log temperature high event on blynk console 
     blynk.log_event('temp_high')
#send warning sound to bluetooth speaker
     call(["aplay", "/home/pi/Assignment/warning.wav"])
#display message on LED screen when temp. event occurs
     sense.set_pixels(flame)
#if statement for min. temperature event
elif temp <= minTemp:
     blynk.virtual_write(1, round((sense.temperature -7),1))
#log temperature low event on blynk console
     blynk.log_event('temp_low')
#send warning sound to bluetooth speaker
     call(["aplay", "/home/pi/Assignment/warning.wav"])
#display message on LED screen when temp. event occurs
     sense.set_pixels(ice)
    else:
     blynk.virtual_write(1, round((sense.temperature -7),1))
#writes the humidity reading to the console
    blynk.virtual_write(2, round(sense.humidity,1))
    sleep(600)
