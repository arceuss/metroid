import math, random
from metroid_config import *
import metroid_utils

def encounter(Samus):
    enemy = metroid_utils.create_enemy("brinstar")
    while enemy.Alive and not enemy.Fleed:
        Samus.attack(enemy)
        enemy.attack(Samus)
    if not enemy.Fleed:
        tmp = Samus.HP
        Samus.HP += random.randint(0,20)
        while Samus.HP > 99:
            Samus.HP -= 99
            Samus.EnergyTanks += 1
            if Samus.EnergyTanks > Samus.MaxEnergyTanks:
                Samus.EnergyTanks = Samus.MaxEnergyTanks
        gained = Samus.HP - tmp
        metroid_utils.type(f"You have restored {gained} energy.",textspeed_status)
    else:
        metroid_utils.type(f"You escaped from battle, so you gained nothing.")