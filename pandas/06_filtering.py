import pandas as pd

def main():
    df = pd.read_csv("data/data.csv")

    tall_pokemon = df[df["Height"] >= 10]
    print(tall_pokemon)

    heavy_pokemon = df[df["Weight"] >= 200]
    print(heavy_pokemon)

    legendary_pokemon = df[df["Legendary"] == True]
    print(legendary_pokemon)

    water_pokemon = df[(df["Type 1"] == "Water") | (df["Type 2"] == "Water")]
    print(water_pokemon)

    fire_and_flying_pokemon = df[(df["Type 1"] == "Fire") & (df["Type 2"] == "Flying")]
    print(fire_and_flying_pokemon)

if __name__ == "__main__":
    main()