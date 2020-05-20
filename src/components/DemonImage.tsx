import React, { useState } from "react";
import { css } from "emotion";

import { Species } from "../demons/index";

export const DemonImage: React.FC<{
  species: Species;
  onClick?: () => void;
}> = ({ species, onClick }) => {
  const [hovered, setHovered] = useState(false);

  const imageType = ["front"];
  if (hovered && onClick) {
    imageType.push("sparklie");
  }
  const paddedNumber = String(species.number).padStart(3, "0");
  const fileName = imageType.join("-") + ".png";
  const path = `/demons/${paddedNumber}-${species.name.toLowerCase()}/${fileName}`;

  return (
    <img
      alt={`${species.name}, Purse Demon #${species.number}`}
      src={path}
      draggable={false}
      onClick={onClick && (() => onClick())}
      onMouseEnter={() => setHovered(true)}
      onMouseLeave={() => setHovered(false)}
      className={css({
        objectFit: "contain",
        imageRendering: "pixelated",
        width: 48,
        height: 48,
        cursor: onClick ? "pointer" : undefined,
        userSelect: onClick ? "none" : undefined,
      })}
    />
  );
};
