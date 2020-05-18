#!/usr/bin/env python3.6
import random

def main():
    """
    Task BINGO-26:
    - give each unit a speed
    - faster unit attacks first
    - if the speed is tied, then decide randomly like we currently do.
    Task BINGO-29:
    - give each *instance* of a unit a distinct name, optionally. like in pokemon.
    """

    kerrigan = Baneling()
    arthas = Battlecruiser()
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
    def __init__(self):
        self.max_hp = 1000
        self.hp = self.max_hp
        self.attack = 40
        self.base_speed = 1

    def __str__(self):
        return f"<Battlecruiser {self.hp}/{self.max_hp} HP, {self.attack} attack>" 

class Baneling(Unit):
    def __init__(self):
        self.max_hp = 10000
        self.hp = self.max_hp
        self.attack = 40
        self.base_speed = 400

    def __str__(self):
        return f"<Baneling {self.hp}/{self.max_hp} HP, {self.attack} attack>"

class Marine(Unit):
    def __init__(self):
        self.max_hp = 40
        self.hp = self.max_hp
        self.attack = 8
        self.base_speed = 100
    
    def __str__(self):
        return f"<Marine {self.hp}/{self.max_hp} HP, {self.attack} attack>"

if __name__ == "__main__":
    main()
