import React from "react";
import ReactDOM from "react-dom";

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
  output.classList.add("printed");

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

  document.body.appendChild(output);
  window.scroll(0, document.body.scrollHeight);
};

print.as = Symbol("print.as");
