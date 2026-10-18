import pandas as pd

def main():
    df = pd.read_csv("data/data.csv", index_col="Name")

    pokemon = input("enter a pokémon name: ")

    try:
        print(df.loc[pokemon])
    except KeyError:
        print(f"{pokemon} not found")

if __name__ == "__main__":
    main()