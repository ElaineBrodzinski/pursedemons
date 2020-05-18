#!/usr/bin/env python3.6
import random
import time

"""
TASK BINGO-BONGO-99:
- Mark units as Air or Ground.
- Mark attacks as Air or Ground or Both.
- Give units multiple attacks, which may be different for air and ground.
- Make units pick attacks based on which is more powerful.
"""

def main():
    kerrigan = Corrupter()
    arthas = Marine()
    fight_to_the_death(kerrigan, arthas)


def fight_to_the_death(red: 'Unit', blue: 'Unit'):
    print("Today! Fighting to the death, for your entertainment, we have.")
    print(f"In the red corner: {red}")
    print(f"In the blue corner: {blue}")


    while red.hp > 0  and blue.hp > 0:
        time.sleep(0.25)

        if red.base_speed > blue.base_speed:
            attack_first = red
        elif blue.base_speed > red.base_speed:
            attack_first = blue
        else:
            attack_first = random.choice([red, blue])

        if attack_first == red:
           attack_second = blue
        else:
           attack_second = red

        attack_first.attack_other(attack_second)

        if red.hp <= 0 or blue.hp <= 0:
           break

        attack_second.attack_other(attack_first)



    print()
    print("--- THE JUDGE'S SCORECARDS ---")
    print(f"red: {red}")
    print(f"blue: {blue}")

class Unit:
    hp: int
    max_hp: int
    attack: int
    base_speed: int
    nickname: str
    position: str
    attack_range: str
    
    def __init__(self, nickname: str = None):
        self.hp = self.max_hp

        if nickname is None:
            nickname = type(self).__name__
        self.nickname = nickname

    def __str__(self):
        return f"<{self.nickname} {self.hp}/{self.max_hp} HP, {self.attack} attack>" 

    def attack_other(self, other_unit: 'Unit'):
        """Have this unit do an attack, reducing the HP of another unit."""

        print(f"{self} is attacking {other_unit}.")
        damage = self.attack


        # like here
            
        if self.attack_range == "universal":
            pass
        else:
            if self.attack_range == "air" and other_unit.position == "ground":
                self.attack = 0 
            if self.attack_range == "ground" and other_unit.position == "air":
                self.attack = 0
        
        if other_unit.attack_range == "universal":
            pass
        else:
            if other_unit.attack_range == "air" and self.position == "ground":
                other_unit.attack = 0 
            if other_unit.attack_range == "ground" and self.position == "air":
                other_unit.attack = 0

        if random.randint(1, 100) <= 5:
            print("It's a critical hit!")
            damage = damage * 2
        other_unit.hp -= damage
        if other_unit.hp <= 0:
            print(f"{other_unit} has been killed by {self}.")
            other_unit.hp = 0

class Battlecruiser(Unit):
    max_hp = 1000
    attack = 40
    attack_range = "universal"
    base_speed = 1
    position = "air"

class Baneling(Unit):
    max_hp = 10000
    attack = 40
    attack_range = "ground"
    base_speed = 400
    position = "ground"

class Marine(Unit):
    max_hp = 40
    attack = 8
    attack_range = "universal"
    base_speed = 100
    position = "ground"

class Corrupter(Unit):
    max_hp = 150
    attack = 30
    attack_range = "air"
    base_speed = 50
    position = "air"
    
if __name__ == "__main__":
    main()
