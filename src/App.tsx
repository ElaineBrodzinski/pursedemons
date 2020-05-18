import React from "react";

import { print } from "./common";
import { Demon } from "./demon";

export class App {
  /// Initialize the application.
  constructor() {
    // TODO: do we have anything to put here?
  }

  /// Run the application.
  async main() {
    for (let x = 0; x < 10; x += 2) {
      print("Hello world!", { x, y: x });
    }
  }

  /// Render the current state of the application to the page.
  render() {
    return (
      <div>
        <p>
          You may want to press <kbd>F12</kbd> to open your developer console.
        </p>

        <p>
          <Demon id={96} />
        </p>
      </div>
    );
  }
}

type Range = "universal" | "air" | "ground";

class Unit {
  hp: number;
  maxHp: number;
  attack: number;
  speed: number;
  nickname: string;
  position: string;
  range: Range;
}
