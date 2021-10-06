textspeed_scale = 100 #default 1

textspeed_encounter = 40 * textspeed_scale
textspeed_damage = 80 * textspeed_scale
textspeed_status = 160 * textspeed_scale
textspeed_options = 160 * textspeed_scale
textspeed_enemydie = 40 * textspeed_scale
textspeed_playerdie = 20 * textspeed_scale
textspeed_menu = 180 * textspeed_scale
textspeed_menu_art = 180 * textspeed_scale

max_energy = 20 # Max number of energy tanks
class Weapon:
    def __init__(self, name, dmg, verb, secondaryverb, aliases=[], combo=[]):
        self.Name = name
        self.Damage = dmg
        self.Verb1 = verb
        self.Combo = combo
        self.Verb2 = secondaryverb
        if aliases == [] and combo == []:
            self.Aliases = [self.Name]
        else:
            self.Aliases = aliases
class BaseEnemy:
    def __init__(self,name,hp,atk,e,be,m,sm,pb,hasArticle=True,fleechance=50,vulnerable=["all"],playerturns=1):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.energy_chance = e
        self.big_energy_chance = be
        self.missile_chance = m
        self.super_missile_chance = sm
        self.power_bomb_chance = pb
        self.has_article = hasArticle
        self.vulnerable = vulnerable
        self.playerturns = playerturns
        self.fleechance = fleechance
weapons = [
    # You (verb1) (name) (verb2) (enemyname), dealing (damage) damage.
    # Base beams
    Weapon("beam", 20, "fire a", "at", ["", "beam", "fire", "shoot", "zap"]),
    Weapon("ice beam", 30, "fire an", "at",["i", "ice"]),
    Weapon("spazer beam", 40, "fire a", "at",["sp","spazer"]),
    Weapon("wave beam", 50, "fire a", "at",["w","wave"]),
    Weapon("plasma beam", 150, "fire a", "at",["p","plasma"]),
    
    # Combo beams
    Weapon("ice+spazer beam", 60, "fire an", "at",[], ["ice beam","spazer beam"]),
    Weapon("ice+wave beam", 60, "fire an", "at",[], ["ice beam","wave beam"]),
    Weapon("wave+spazer beam", 70, "fire a", "at",[], ["wave beam","spazer beam"]),
    Weapon("ice+wave+spazer beam", 100, "fire an", "at",[], ["ice beam", "wave beam", "spazer beam"]),
    Weapon("ice+plasma beam", 200, "fire an", "at",[], ["ice beam", "plasma beam"]),
    Weapon("wave+plasma beam", 250, "fire a", "at",[], ["wave beam", "plasma beam"]),
    Weapon("ice+wave+plasma beam", 300, "fire an", "at",[], ["ice beam", "wave beam", "plasma beam"]),
    
    # Other combos
    Weapon("charged bombs", 50, "throw some", "at", [], ["beam", "bomb"]),
    
    # Shields
    Weapon("shield", 0, "defend with a", "against", ["sh","shield"]),
    Weapon("wave shield", 300, "defend with a", "against",[], ["shield", "wave beam"]),
    Weapon("ice shield", 90, "defend with an", "against",[], ["shield", "wave beam"]),
    Weapon("spazer shield", 300, "defend with a", "against",[], ["shield", "wave beam"]),
    Weapon("plasma shield", 300, "defend with a", "against",[], ["shield", "wave beam"]),
    
    # Missiles/Bombs
    Weapon("missile", 100, "launch a", "at",["m","missile"]),
    Weapon("super missile", 300, "launch a", "at",["sm","super missile","s missile"]),
    Weapon("bomb", 10, "throw a", "at",["b","bomb"]),
    Weapon("power bomb", 200, "throw a", "at",["pb","power bomb", "p bomb"]),
    
    # Flee-type moves
    Weapon("high jump boots", 0, "flee with your", ["flee","f","run","escape","abscond"]),
    Weapon("screw attack", 1000, "flee with your", ["screw","s"]),
]
enemies = [
    #BaseEnemy("Geemer",15,5,22,10,66,2,0),
    #BaseEnemy("Silver Geemer", 15, 5, 51, 8, 0, 0, 2),
    BaseEnemy("Kihunter", 60, 20, 20, 12, 31, 4, 4),
    #BaseEnemy("Yellow Kihunter", 360, 60, 22, 31, 4, 24, 4),
    #BaseEnemy("Red Kihunter", 1800, 200, 14, 47, 4, 24, 4),
    #BaseEnemy("Pink Wall-Mounted Space Pirate", 300, 160, 12, 27, 31, 2, 0),
    #BaseEnemy("Torizo", 800, 8, 20, 20, 20, 20, 20),
    #BaseEnemy("Golden Torizo", 13500, 160, 20, 20, 20, 20, 20),
    BaseEnemy("Side Hopped", 320, 80, 8, 8, 22, 22, 2),
    BaseEnemy("7inches", 320, 80, 8, 8, 22, 22, 2),
    #BaseEnemy("Blue Side Hopped", 1500, 120, 8, 8, 22, 22, 2),
    BaseEnemy("Space Pirate", 20, 15, 20, 47, 31, 2, 0),
    #BaseEnemy("Green Space Pirate", 90, 20, 20, 12, 39, 8, 4),
    #BaseEnemy("Red Space Pirate", 200, 80, 4, 8, 8, 2, 2),
    #BaseEnemy("Pink Space Pirate", 300, 160, 20, 47, 31, 2, 0),
    #BaseEnemy("Yellow Space Pirate", 900, 200, 20, 47, 31, 2, 0),
    #BaseEnemy("Silver Space Pirate", 1800, 100, 0, 59, 2, 39, 0),
    BaseEnemy("Reo", 45, 15, 12, 31, 33, 4, 4),
    BaseEnemy("Ripper", 200, 5, 31, 8, 31, 2, 2),
    #BaseEnemy("Mellow Hive", 54, 48, 20, 27, 31, 2, 0),
    #BaseEnemy("Tripper", 1, 1, 31, 31, 31, 2, 2, True, []),
    BaseEnemy("Waver", 30, 10, 24, 24, 24, 24, 3),
    BaseEnemy("Skree", 30, 10, 8, 1, 33, 2, 2, 50, True, [], 2),
    #BaseEnemy("Kago Hive", 90, 24, 20, 35, 27, 8, 8),
    #BaseEnemy("Alcoon", 200, 50, 1, 0, 0, 0, 99),
    #BaseEnemy("Yapping Maw", 20, 20, 0, 0, 0, 0, 0, True, ["super missile"]),
    #BaseEnemy("Sciser", 200, 120, 1, 39, 0, 0, 60, True, ["all"], 3),
    BaseEnemy("Boyon", 1000, 10, 8, 4, 33, 2, 2),
    #BaseEnemy("Choot", 100, 80, 24, 24, 24, 24, 3, True, ["all"], 2),
    BaseEnemy("Metaree", 100, 50, 3, 10, 31, 2, 2, 50, True, [], 2),
    BaseEnemy("Zebbo Swarm", 180, 120, 0, 75, 10, 50, 5),# Sprite: zebbo's flying out of a pipe
    #
    BaseEnemy("Fireflea", 20, 4, 0, 1, 0, 0, 99),
    #
    BaseEnemy("Ripper II", 200, 10, 0, 1, 0, 99, 0),
    #
    BaseEnemy("Cacatac", 60, 20, 0, 1, 0, 99, 0),
    BaseEnemy("Small Side Hopper", 60, 20, 8, 16, 33, 2, 2),
    BaseEnemy("Zero",50,40,1,0,0,0,99),
    #BaseEnemy("Mini-Kraid", 400, 100, 0, 1, 0, 99, 0, False),
    #BaseEnemy("Puyo", 100, 60, 24, 24, 24, 3, 24),
    #
    #BaseEnemy("Mella", 90, 48, 40, 25, 30, 5, 0),
    #
    
]
