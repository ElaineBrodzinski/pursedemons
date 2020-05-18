import React from "react";
import ReactDOM from "react-dom";

import { App } from "./app";

setTimeout(async () => {
  const app = new App();
  const root = document.querySelector("main");
  const onFrame = () => {
    const content = app.render();
    ReactDOM.render(<React.StrictMode>{content}</React.StrictMode>, root);
    requestAnimationFrame(onFrame);
  };
  onFrame();
  await app.main();
});
