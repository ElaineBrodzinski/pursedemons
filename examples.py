"""

Baneling
- [1] banelings explode
Marine
- [8] stim as an upgrade
- [9] stim expires after a certain time
Battlecruiser
- [2] ignoring flying for now
Overlord

#Banelings are awesome
#dunder

superclass = units  

Battlecruisers, Banelings, Marines 


"""

class Unit:
    def attack_other(self, other_unit):
      other_unit.hp -= self.attack
      if other_unit.hp <= 0:
          other_unit.hp = 0
          print("Battlestation operational.")    

class Battlecruiser(Unit):
    def __init__(self):
        self.hp = 200
        self.max_hp = 200
        self.attack = 40
        
        self.yamato = NotImplemented
        self.recall = NotImplemented

    def __str__(self):
        return f"<Battlecruiser {self.hp}/{self.max_hp} HP, {self.attack} attack>" 

class Baneling(Unit):
    def __init__(self):
        self.hp = 40
        self.max_hp = 40
        self.attack = 40

        self.burrow = NotImplemented
        self.boom = NotImplemented

    def __str__(self):
        return f"<Baneling {self.hp}/{self.max_hp} HP, {self.attack} attack>"

class Marine(Unit):
    def __init__(self):
        self.hp = 40
        self.max_hp = 40
        self.attack = 8
    
    def __str__(self):
        return f"<Marine {self.hp}/{self.max_hp} HP, {self.attack} attack>"

    def stim(self):
        self.hp = self.hp - 10
        self.attack = 12

bob = Baneling()
joe = Baneling()


print("Joe =", joe, "Bob =", bob)
print("Joe attacks Bob")
joe.attack_other(bob)

print("Joe =", joe, "Bob =", bob)
