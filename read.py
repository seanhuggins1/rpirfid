import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import beepy

reader = SimpleMFRC522()

print(beepy.beep)

while(True):
    print("Waiting for you to scan an RFID sticker/card")
    id = reader.read()[0]
    print("The ID for this card is: ", id)
    beepy.beep(sound=1)
    print("Waiting before scanning again...")
    time.sleep(3)