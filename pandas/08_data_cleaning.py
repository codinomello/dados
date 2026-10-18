import pandas as pd

def main():
    df = pd.read_csv("data/data.csv")

    df["Name"] = df["Name"].str.lower()
    print(df.to_string())

    df["Legendary"] = df["Legendary"].astype(bool)
    print(df.to_string())

    df = df.drop_duplicates()
    print(df.to_string())


    df["Type 1"] = df["Type 1"].replace({
        "Fire": "FIRE",
        "Water": "WATER",
        "Grass": "GRASS"
    })
    print(df.to_string())

    df = df.drop(columns=["Legendary", "No"])
    print(df.to_string())

    df = df.dropna(subset=["Type 2"])
    print(df.to_string())

    df = df.fillna({"Type 2": "None"})
    print(df.to_string())

if __name__ == "__main__":
    main()