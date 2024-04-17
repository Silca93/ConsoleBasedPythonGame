class Hero:
    def __init__(self, name, hp, maxHp, atk, armor, lvl, items, gold, place):
        self.name = name
        self.maxHp = maxHp
        self.hp = hp
        self.atk = atk
        self.armor = armor
        self.lvl = lvl
        self.items = items
        self.gold = gold
        self.place = place

        
# _______________________________________

class Witch(Hero):
    def __init__(self, name, hp, maxHp, atk, sp_atk,  armor, lvl, items, gold, place):
        super().__init__(name, hp, maxHp, atk, armor, lvl, items, gold, place)
        self.sp_atk = sp_atk

    def frozen_orb(self):
        print(f"You used frozen orb! You have: {self.gold} gold") 

witch_hero = Witch("Merion", 100, 100,  20, 40, 10, 1, [], 50, "village")       
# __________________________________________________________    

class Paladin(Hero):
    def __init__(self, name, hp, maxHp, atk, armor, lvl, items, gold, shield, place):
        super().__init__(name, hp, maxHp, atk, armor, lvl, items, gold, place)
        self.shield = shield
        
    def holy_hammer(self):
        print("You used holy hammer!") 

paladin_hero = Paladin("Cirat", 140, 140, 40, 25, 1, [], 50, True, "village")           

# ____________________________________________________________
class Barbarian(Hero):
    def __init__(self, name, hp, maxHp, atk, armor, lvl, items, gold, prospection, place):
        super().__init__(name, hp, maxHp, atk, armor, lvl, items, gold, place)
        self.prospection = prospection
        
    def iron_skin(self):
        print("You used iron skin!") 
        self.armor = 35  

barbarian_hero = Barbarian("Bigboy", 140, 140, 40, 25, 1, [], 50, 1.5, "village")   



#____________________________________________
# class Places:
#     def __init__(self,)


#//? ___________________________________________

class Enemy:
    def __init__(self, name, hp, maxHp, atk, armor, lvl):
        self.name = name
        self.hp = hp
        self.maxHp = maxHp
        self.atk = atk
        self.armor = armor
        self.lvl = lvl

# _____________________________________________
class Mob(Enemy):
    def __init__(self, name, hp, maxHp, atk, armor, lvl):
        super().__init__(name, hp, maxHp, atk, armor, lvl)

    def normal_attack(self, damage):
        #  damage = atk
        self.damage = 15


creep = Mob("skeleton", 40, 40, 15, 10, 1)     

# ___________________________________________________

class Boss(Enemy):
    def __init__(self, name, hp, maxHp, atk, armor, lvl):
        super().__init__(name, hp, maxHp, atk, armor, lvl)

    def Boss_attack(self, damage):
        #  damage = atk
        self.atk = 20


Steven = Boss("Stevenosaurus-Rex", 100, 100, 30 , 15, 4)         

#//? ___________________________________________

class Inventory:
    def __init__(self):
        self.content = []

    def add(self, items):
        self.content.append(items)