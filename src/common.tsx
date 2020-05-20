import React from "react";
import ReactDOM from "react-dom";
import { css, keyframes } from "otion";

export const sleep = (seconds: number) =>
  new Promise((resolve) => setTimeout(resolve, seconds * 1000));

export const randomChoice = <Value extends unknown = unknown>(
  values: Iterable<Value>,
): Value => {
  const valueArray = [...values];
  if (valueArray.length === 0) {
    throw new Error("can't select random value from empty array!");
  }
  const index = Math.floor((valueArray.length - 1) * Math.random());
  return valueArray[index];
};

export const print = (...values: Array<any>) => {
  console.log(...values);

  const output = document.createElement("p");
  output.className = css({
    animationName: `${keyframes({
      "0%": { opacity: 0.0 },
      "5%": { opacity: 1.0 },
      "25%": { opacity: 1.0 },
      "50%": { opacity: 0.5 },
      "100%": { opacity: 1.0 },
    })}`,
    animationDuration: "8s",
    animationIterationCount: 1,
    animationFillMode: "forwards",
  });

  for (let value of values) {
    while (typeof value?.[print.as] === "function") {
      value = value[print.as]();
    }

    if (
      React.isValidElement(value) ||
      typeof value == "string" ||
      typeof value == "number"
    ) {
      const el = document.createElement("span");
      ReactDOM.render(<React.StrictMode>{value}</React.StrictMode>, el);
      output.appendChild(el);
    } else {
      const el = document.createElement("code");
      el.textContent =
        typeof value === "object"
          ? JSON.stringify(value, null, 2)
          : String(value);
      output.appendChild(el);
    }

    output.appendChild(document.createTextNode(" "));
  }

  const oldMax =
    window.document.documentElement.scrollHeight - window.innerHeight;
  const atBottom = window.document.documentElement.scrollTop >= oldMax - 4;

  document.body.appendChild(output);

  const newMax =
    window.document.documentElement.scrollHeight - window.innerHeight;

  if (atBottom) {
    window.document.documentElement.scrollTop = newMax;
  }
};

print.as = Symbol("print.as");
