import React, { useState } from "react";
import { css } from "otion";

export const DemonImage: React.FC<{ name: string; number: number }> = ({
  name,
  number,
}) => {
  const [hovered, setHovered] = useState(false);

  const imageType = ["front"];
  if (hovered) {
    imageType.push("sparklie");
  }
  const paddedNumber = String(number).padStart(3, "0");
  const fileName = imageType.join("-") + ".png";
  const path = `/prdm/${paddedNumber}-${name.toLowerCase()}/${fileName}`;

  return (
    <img
      alt={`${name}, Purse Demon #${number}`}
      src={path}
      draggable={false}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      className={css({
        objectFit: "contain",
        imageRendering: "pixelated",
        width: 48,
        height: 48,
      })}
    />
  );
};
