import React from "react";

export const Demon: React.FC<{ id: number }> = ({ id }) => {
  return <img src={`/prdm/${id}/front.png`} alt={`Demon #${id}`} />;
};
