import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import beepy

reader = SimpleMFRC522()

def readId():
    id = reader.read()[0]
    return id