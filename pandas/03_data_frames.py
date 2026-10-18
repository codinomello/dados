import pandas as pd

def main():
    data = {
        "name": ["spongebob", "patrick", "squidward", "sandy"],
        "age": [20, 21, 30, 25],
    }
    df = pd.DataFrame(data, index=["character #1", "character #2", "character #3", "character #4"])
    
    df["occupation"] = ["cook", "unemployed", "cashier", "scientist"]
    
    new_row = pd.DataFrame([{"name": "mr. krabs", "age": 55, "occupation": "manager"}], index=["manager"])
    df = pd.concat([df, new_row])

    print(f"data frame:\n{df}")

if __name__ == "__main__":
    main()