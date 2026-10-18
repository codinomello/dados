import numpy as np

def main():
    ages = np.array([6, 8, 9, 12, 13, 17, 18, 22, 25, 31, 37, 42, 48, 53, 59, 65, 66, 71, 72, 83, 89])
    print(f"ages array: {ages}")
    
    teenagers = ages[ages < 18]
    print(f"teenagers (ages < 18): {teenagers}")

    adults = ages[(ages >= 18) & (ages < 65)]
    print(f"adults (ages >= 18): {adults}")

    seniors = ages[ages >= 65]
    print(f"seniors (ages >= 65): {seniors}")

    evens = ages[ages % 2 == 0]
    print(f"even ages: {evens}")

    odds = ages[ages % 2 != 0]
    print(f"odd ages: {odds}")

    substituted_ages = np.where(ages >= 18, ages, ":)")
    print(f"ages with teenagers substituted by 18: {substituted_ages}")

if __name__ == "__main__":
    main()