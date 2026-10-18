import pandas as pd

def main():
    df = pd.read_csv("data/data.csv")

    df_mean = df.mean(numeric_only=True)
    print(f"average:\n{df_mean}")
    
    df_sum = df.sum(numeric_only=True)
    print(f"sum:\n{df_sum}")
    
    df_min = df.min(numeric_only=True)
    print(f"minimun:\n{df_min}")

    df_max = df.max(numeric_only=True)
    print(f"maximum:\n{df_max}")
    
    df_count = df.count(numeric_only=True)
    print(f"count of each{df_count}")

    df_shape = df.shape[0]
    print(f"shape: {df_shape}")

    grouped_by_type1 = df.groupby("Type 1")
    print(f"average by type 1:\n{grouped_by_type1.mean(numeric_only=True)}")
    grouped_by_legendary = df.groupby("Legendary")
    print(f"average by legendary:\n{grouped_by_legendary.mean(numeric_only=True)}")

if __name__ == "__main__":
    main()