import sys
from art import text2art as ascii
from metroid_utils import *
from metroid_config import *
from data.objects import *
from data.battle import *

type(ascii("METROID"),textspeed_menu_art)

type('1. New Game',textspeed_menu)
type('2. Load Game',textspeed_menu)

type("Press the corresponding key for an option, then hit enter to confirm.",textspeed_menu)

menuoption = input("> ").upper()
print()

if menuoption == '1':
    type("Starting New Game...", textspeed_menu)
    Samus = Player()
    while True:
        encounter(Samus)
        input("> ")
        print()
elif menuoption == '2':
    type("Locate the path of your save file.", textspeed_menu)
else:
    type("Quitting...", textspeed_menu)
    sys.exit()