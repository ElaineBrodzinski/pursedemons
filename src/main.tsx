import React from "react";

import { print, sleep, randomChoice } from "./common";
import { DemonImage } from "./components/DemonImage";
import { css } from "otion";

export class App {
  /// Run the application.
  async main() {
    await fightToTheDeath(new Tagger(), new Ursa());
  }

  /// Render the current state of the application to the page.
  render() {
    const height = 256;

    return (
      <>
        <div className={css({ display: "block", height })}></div>
        <div
          className={css({
            display: "block",
            position: "fixed",
            left: 0,
            right: 0,
            top: 0,
            padding: 16,
            height,
            borderBottom: "1px solid black",
            background: "white",
            zIndex: 1000,
          })}
        >
          <p>{new Tagger().renderCard()}</p>

          <p>{new Tagger().renderCard()}</p>
        </div>
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
    await sleep(1.0);

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
  name: string;
  number: number;
  hp: number;
  maxHp: number;
  attack: number;
  speed: number;
  nickname: string;
  position: string;
  range: string;
  image: string;

  [print.as]() {
    return this.renderCard(false);
  }

  renderCard(healable = true) {
    const vitality = this.hp / this.maxHp;
    const color =
      vitality >= 1.0
        ? "#88E0D0"
        : vitality >= 0.8
        ? "#8DA"
        : vitality >= 0.4
        ? "#DA4"
        : vitality >= 0.2
        ? "#E93"
        : vitality > 0
        ? "#F00"
        : "#402";
    return (
      <span
        className={css({
          padding: 4,
          borderRadius: 4,
          border: "1px solid #888",
          width: 256,
          position: "relative",
        })}
      >
        <DemonImage
          name={this.name}
          number={this.number}
          onClick={
            healable
              ? () => {
                  this.hp = this.maxHp;
                  print("You healed ", this);
                }
              : undefined
          }
        />{" "}
        <span
          className={css({
            display: "inline-block",
            width: 80,
            fontWeight: "bold",
          })}
        >
          {this.nickname}
        </span>{" "}
        <code
          className={css({
            display: "inline-block",
            width: 150,
            fontWeight: "bold",
            textAlign: "right",
          })}
        >
          {this.hp}/{this.maxHp} HP
        </code>
        <span
          className={css({
            position: "absolute",
            bottom: 0,
            left: 0,
            right: 100 - 100 * vitality + "%",
            transition: "all 0.5s ease-out",
            height: 4,
            background: color,
            zIndex: -32,
          })}
        ></span>
        <span
          className={css({
            opacity: 1 / 4,
            position: "absolute",
            bottom: 0,
            left: 0,
            right: 0,
            height: 5,
            borderTop: "1px solid black",
            transition: "all 0.5s ease-out",
            background: color,
            zIndex: -64,
          })}
        ></span>
      </span>
    );
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

class Tagger extends Unit {
  constructor() {
    super();

    this.name = "Tagger";
    this.number = 96;
    this.nickname = this.name;
    this.maxHp = 100;
    this.hp = this.maxHp;
    this.attack = 40;
    this.range = "universal";
    this.speed = 1;
    this.position = "air";
  }
}

class Ursa extends Unit {
  constructor() {
    super();

    this.name = "Ursa";
    this.number = 111;
    this.nickname = this.name;
    this.maxHp = 100;
    this.hp = this.maxHp;
    this.attack = 40;
    this.range = "universal";
    this.speed = 400;
    this.position = "ground";
  }
}

class Ursus extends Unit {
  constructor() {
    super();

    this.name = "Ursus";
    this.number = 112;
    this.nickname = this.name;
    this.maxHp = 200;
    this.hp = this.maxHp;
    this.attack = 8;
    this.range = "universal";
    this.speed = 100;
    this.position = "ground";
  }
}
