export type Species = {
  readonly number: number;
  readonly name: string;
  readonly evolvesFrom: "none" | "egg" | Species["number"];
};

const species: Array<Species> = [];
export const demons: Readonly<Array<Readonly<Species>>> = species;

const declareSpecies = (
  number: Species["number"],
  name: Species["name"],
  evolvesFrom: Species["evolvesFrom"] = "none",
): Species => {
  const demon: Species = { number, name, evolvesFrom };
  if (species[demon.number]) {
    throw new Error(`duplicate demon species number: ${demon.number}`);
  }
  if (species[demon.name] || species[demon.name.toLowerCase()]) {
    throw new Error(`duplicate demon species name: ${demon.name}`);
  }
  species[demon.number] = demon;
  species[demon.name] = demon;
  species[demon.name.toLowerCase()] = demon;
  return demon;
};

export const tagger = declareSpecies(96, "Tagger");
export const ursa = declareSpecies(111, "Ursa", "egg");
export const ursus = declareSpecies(112, "Ursus", ursa.number);
export const violetsky = declareSpecies(144, "Violetsky", "egg");
