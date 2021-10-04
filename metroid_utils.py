import sys
import time
import random
import ascii_magic
from metroid_config import *

def pick(options):
    type("Select an option.",textspeed_options)
    for idx, element in enumerate(options):
        ("{}) {}".format(idx+1,element),160)
    i = input("> ")
    print()
    try:
        if 0 < int(i) <= len(options):
            return int(i)
    except:
        pass
    return None
def type(text,speed):
    for letter in text + "\n\n":
        sys.stdout.write(letter)
        sys.stdout.flush()
        #time.sleep(1.0/speed) # speed = number of times per second
def render(imagepath,color):
    if not color:
        color = ascii_magic.Modes.ASCII
    else:
        color = ascii_magic.Modes.TERMINAL
    ascii_magic.to_terminal(ascii_magic.from_image_file(
        imagepath,
        columns = 100,
        mode = color))
def create_enemy(region):
    if region == "brinstar":
        enemytype = enemies[random.randint(0,len(enemies)-1)]
        import data.objects
        return data.objects.Enemy(enemytype.name, enemytype.hp, enemytype.atk, enemytype.energy_chance, enemytype.big_energy_chance, enemytype.missile_chance, enemytype.super_missile_chance, enemytype.power_bomb_chance, enemytype.has_article, enemytype.vulnerable, enemytype.playerturns, enemytype.fleechance)