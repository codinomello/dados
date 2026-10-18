import pandas as pd

def main():
    data = [1, 2, 3, 4, 5]
    series = pd.Series(data)
    print(f"series:\n{series}")

    prices = [10.5, 20.75, 30.0, 40.25, 50.5]
    price_series = pd.Series(prices, index=['apple', 'banana', 'cherry', 'date', 'elderberry'])
    print(f"\nprice series:\n{price_series}")
   
    statements = [True, False, True, False]
    statements_series = pd.Series(statements)
    print(f"\nstatements series:\n{statements_series}")

    abc = {'a': 'A', 'b': 'B', 'c': 'C'}
    abc_series = pd.Series(abc)
    print(f"\nseries from dictionary:\n{abc_series}")

    abc_series.loc['a'] = "Alpha"
    print(f"\nelement at index 'a': {abc_series.loc["a"]}")
    print(f"element at index '1': {abc_series.iloc[1]}")

    bin = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    bin_series = pd.Series(bin)
    print(f"\n{bin_series[bin_series < 256]}")

    cals = {"day 1": 420, "day 2": 380, "day 3": 390}
    cals_series = pd.Series(cals)

    cals_series.iloc[2] += 20
    cals_series.loc['day 4'] = 430

    print(f"\ncalories series:\n{cals_series}")

if __name__ == "__main__":
    main()