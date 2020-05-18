#!/usr/bin/env python3.6
import random

def main():
    kerrigan = Baneling("Kerrigan")
    arthas = Battlecruiser("Arthas")
    fight_to_the_death(kerrigan, arthas)


def fight_to_the_death(red: 'Unit', blue: 'Unit'):
    print("Today! Fighting to the death, for your entertainment, we have.")
    print(f"In the red corner: {red}")
    print(f"In the blue corner: {blue}")

    while red.hp > 0  and blue.hp > 0:
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
    base_speed = 1

class Baneling(Unit):
    max_hp = 10000
    attack = 40
    base_speed = 400

class Marine(Unit):
    max_hp = 40
    attack = 8
    base_speed = 100
    
if __name__ == "__main__":
    main()
