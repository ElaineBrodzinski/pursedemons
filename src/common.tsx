import React from "react";
import ReactDOM from "react-dom";

export const print = (...values: Array<any>) => {
  console.log(...values);

  const output = document.createElement("p");
  output.classList.add("printed");

  for (const value of values) {
    if (
      React.isValidElement(value) ||
      typeof value === "string" ||
      typeof value === "number"
    ) {
      const el = document.createElement("span");
      ReactDOM.render(<React.StrictMode>{value}</React.StrictMode>, el);
      output.appendChild(el);
    } else {
      const el = document.createElement("code");
      el.textContent = JSON.stringify(value, null, 2);
      output.appendChild(el);
    }
    output.appendChild(document.createTextNode(" "));
  }

  document.body.appendChild(output);
  window.scroll(0, document.body.scrollHeight);
};
