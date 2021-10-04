import metroid_utils
from metroid_config import *
import sys
import random
import os
class Enemy:
    #def __init__(self,name,hp,atk,e,be,m,sm,pb,hasArticle=True,vulnerable=["all"],playerturns=1):
    def __init__(self,name,hp,atk,e,be,m,sm,pb,hasArticle,vulnerable,playerturns,fleechance):
        self.Name = name
        self.HP = hp
        self.MHP = hp
        self.DMG = atk
        self.energy_chance = e
        self.big_energy_chance = be
        self.missile_chance = m
        self.super_missile_chance = sm
        self.power_bomb_chance = pb
        self.vulnerable = vulnerable
        self.playerturns = playerturns
        self.turnnumber = 1
        self.Alive = True
        self.Fleed = False
        self.fleechance = fleechance
        self.frozenturns = 0
        self.hasArticle = hasArticle # used for things where you would want to prevent a name like "the Kraid" -- used in titledname
        if os.path.isfile(f'assets/enemies/{self.Name}.png'):
            metroid_utils.render(f'assets/enemies/{self.Name}.png',True)
        elif os.path.isfile(f'assets/enemies/{self.Name}'):
            metroid_utils.render(f'assets/enemies/{self.Name}',True)
        elif os.path.isfile(f'assets/enemies/Arachnus.png'):
            metroid_utils.render(f'assets/enemies/Arachnus.png',True)
        elif os.path.isfile(f'assets/enemies/Arachnus'):
            metroid_utils.render(f'assets/enemies/Arachnus',True)
        else:
            print(f"Could not find image file for: '{self.Name}' or default Arachnus image")
            sys.exit()
        metroid_utils.type(f"You encounter {self.indefinitearticle_name()}!",textspeed_encounter)
        metroid_utils.type(f"Health: {self.HP}",textspeed_encounter)
        metroid_utils.type(f"Damage: {self.DMG}",textspeed_encounter)
    def attack(self,opponent):
        if self.frozenturns == 0 and self.turnnumber % self.playerturns == 0:
            if self.Alive and not self.Fleed:
                opponent.take_damage(self.DMG)
                metroid_utils.type(f"{self.definitearticle_name().title()} damages you for {self.DMG} energy!",textspeed_damage)
            else:
                metroid_utils.type(f"{self.definitearticle_name().title()} has died.",textspeed_enemydie)
        elif self.frozenturns > 0:
            self.frozenturns -= 1
        self.turnnumber += 1
    def definitearticle_name(self): 
        if self.hasArticle:
            return "the " + self.Name.title()
        else:
            return self.Name.title()
    def indefinitearticle_name(self):
        if self.hasArticle:
            if self.Name.startswith(('a','e','i','o','u')):
                return "an " + self.Name.title()
            else:
                return "a " + self.Name.title()
        else:
            return self.Name.title()
    def take_damage(self, amount):
        self.HP -= amount
        if self.HP <= 0:
            self.Alive = False
        else:
            metroid_utils.type(f"{self.definitearticle_name().title()} is at {self.HP} HP.",textspeed_status)
    def try_flee(self):
        if (random.random() * 100) <= self.fleechance:
            self.take_damage(self.HP)
            self.Fleed = True
            metroid_utils.type(f"You managed to successfully flee from {self.definitearticle_name()}.")
class Player:
    def __init__(self):
        self.MaxEnergyTanks = 0
        self.EnergyTanks = 0
        self.Weapons = []
        for i in range(len(weapons)):
            self.Weapons.append(i)
        self.HP = 30
        self.ChargedWeapons = []
    def get_max_hp(self):
        return self.MaxEnergyTanks * 99 + 99 # + 99 for the base 99 health
    def take_damage(self, amount):
        self.HP -= amount
        while self.HP <= 0:
            self.EnergyTanks -= 1
            self.HP += 99
            if self.EnergyTanks < 0:
                metroid_utils.type(f"You have died.",textspeed_playerdie)
                sys.exit()
    def attack(self,opponent):
        aligningspace = ""
        if self.HP < 10:
            aligningspace = " " # add a space for health in the single digits -- this lines up the [etanks] part and the ones digit for a tiny bit of polish
        if self.MaxEnergyTanks == 0:
            metroid_utils.type(f"Energy: {aligningspace}{self.HP}",textspeed_status)
        else:
            etanks = "■"*self.EnergyTanks + "□"*(self.MaxEnergyTanks-self.EnergyTanks)
            metroid_utils.type(f"Energy: {aligningspace}{self.HP} [{etanks}]",textspeed_status)
        weapon = None
        charge = False
        while weapon is None:
            choice = input("> ").lower()
            print()
            spl = choice.strip().split(" ")
            charge = False
            if spl[0] == "charge" or spl[0] == "ch" or spl[0] == "combo" or spl[0] == "c":
                choice = ""
                charge = True
                for part in range(1, len(spl)):
                    choice += spl[part] + " "
                choice = choice.strip()
            for weap in self.Weapons:
                for alias in weapons[weap].Aliases:
                    if choice == alias:
                        weapon = weapons[weap]
        if not charge:
            if self.ChargedWeapons == []:
                opponent.take_damage(weapon.Damage)
                metroid_utils.type(f"You {weapon.Verb1} {weapon.Name.title()} {weapon.Verb2} {opponent.definitearticle_name()}, dealing {weapon.Damage} damage.", textspeed_damage)
                return
            self.ChargedWeapons.append(weapon.Name)
            chargedweapon = []
            for weap in weapons:
                if weap.Combo == []:
                    continue
                inlist = True
                for req in weap.Combo:
                    if req not in self.ChargedWeapons:
                        inlist = False
                        break
                if inlist:
                    chargedweapon.append(weap)
            if chargedweapon == []:
                opponent.take_damage(weapon.Damage)
                metroid_utils.type(f"You {weapon.Verb1} {weapon.Name.title()} {weapon.Verb2} {opponent.definitearticle_name()}, dealing {weapon.Damage} damage.", textspeed_damage)
            else:
                chosen = None
                for weap in chargedweapon:
                    if chosen == None or weap.Damage > chosen.Damage:
                        chosen = weap
                opponent.take_damage(chosen.Damage)
                metroid_utils.type(f"You {chosen.Verb1} {chosen.Name.title()} {chosen.Verb2} {opponent.definitearticle_name()}, dealing {chosen.Damage} damage.", textspeed_damage)
            self.ChargedWeapons = []
        else:
            self.ChargedWeapons.append(weapon.Name)