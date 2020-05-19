import React from "react";
import { css } from "otion";

import { print, sleep, randomChoice } from "./common";
import { DemonImage } from "./components/DemonImge";

let _ = `
TASK BINGO-BONGO-99:
- Mark units as Air or Ground.
- Mark attacks as Air or Ground or Both.
- Give units multiple attacks, which may be different for air and ground.
- Make units pick attacks based on which is more powerful.
`;

export class App {
  /// Run the application.
  async main() {
    const kerrigan = new Corruptor();
    kerrigan.nickname = "Kerrigan";

    const someTerran = new Marine();

    await fightToTheDeath(kerrigan, someTerran);
  }

  /// Render the current state of the application to the page.
  render() {
    return (
      <>
        <p>
          <DemonImage
            name="Tagger"
            number={96}
            onClick={() => print("rawr!")}
          />
          Tagger with 10/10 HP.
        </p>

        <p>
          <DemonImage name="Ursa" number={111} />
          Ursa with 11/11 HP.
        </p>
      </>
    );
  }
}

const fightToTheDeath = async (red: Unit, blue: Unit) => {
  print("--- WELCOME TO THE MAIN EVENT! ---");
  print("Today! Fighting to the death, for your entertainment, we have...");
  print("In the red corner:", red);
  print("In the blue corner:", blue);

  while (red.hp > 0 && blue.hp > 0) {
    await sleep(0.25);

    let attackFirst: Unit;
    if (red.speed > blue.speed) {
      attackFirst = red;
    } else if (blue.speed > red.speed) {
      attackFirst = blue;
    } else {
      attackFirst = randomChoice([red, blue]);
    }

    let attackSecond: Unit;
    if (attackFirst === red) {
      attackSecond = blue;
    } else {
      attackSecond = red;
    }

    attackFirst.attackOther(attackSecond);

    if (red.hp <= 0 || blue.hp <= 0) {
      break;
    }

    attackSecond.attackOther(attackFirst);
  }

  print();
  print("--- THE JUDGE'S SCORECARDS ---");
  print("red:", red);
  print("blue:", blue);
};

abstract class Unit {
  hp: number;
  maxHp: number;
  attack: number;
  speed: number;
  nickname: string;
  position: string;
  range: string;

  constructor() {
    this.nickname = this.constructor.name;
  }

  [print.as]() {
    return `<${this.nickname} ${this.hp}/${this.maxHp} HP, ${this.attack} attack>`;
  }

  /// Have this unit perform an attack, reducing the HP of another unit.
  attackOther(otherUnit: Unit) {
    print(this, "is attacking", otherUnit);

    let damage: number;
    if (this.range === "air" && otherUnit.position === "air") {
      damage = 0;
    } else if (this.range === "ground" && otherUnit.position !== "ground") {
      damage = 0;
    } else {
      damage = this.attack;
    }

    if (damage > 0) {
      if (Math.random() < 0.05) {
        print("It's a critical hit!");
        damage = damage * 2;
      }

      otherUnit.hp -= damage;
      if (otherUnit.hp <= 0) {
        otherUnit.hp = 0;
        print(otherUnit, "has been killed by", this);
      }
    }
  }
}

class Battlecruiser extends Unit {
  constructor() {
    super();

    this.maxHp = 1000;
    this.hp = this.maxHp;
    this.attack = 40;
    this.range = "universal";
    this.speed = 1;
    this.position = "air";
  }
}

class Baneling extends Unit {
  constructor() {
    super();

    this.maxHp = 10000;
    this.hp = this.maxHp;
    this.attack = 40;
    this.range = "ground";
    this.speed = 400;
    this.position = "ground";
  }
}

class Marine extends Unit {
  constructor() {
    super();

    this.maxHp = 40;
    this.hp = this.maxHp;
    this.attack = 8;
    this.range = "universal";
    this.speed = 100;
    this.position = "ground";
  }
}

class Corruptor extends Unit {
  constructor() {
    super();

    this.maxHp = 150;
    this.hp = this.maxHp;
    this.attack = 30;
    this.range = "air";
    this.speed = 50;
    this.position = "air";
  }
}
