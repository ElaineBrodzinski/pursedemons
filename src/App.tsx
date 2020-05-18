import React from "react";
import { css } from "otion";

const App: React.FC = () => {
  return <p className={css({ color: "blue" })}>I am blue</p>;
};

export default App;
