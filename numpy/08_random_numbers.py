import numpy as np

def main():
    rng = np.random.default_rng(seed=42)
    print(f"random number generator: {rng}")

    random_int = rng.integers(0, 10)
    print(f"random integer [0, 10): {random_int}")
    
    random_int = rng.integers(low=10, high=100, size=(3, 2))
    print(f"random integer [10, 100):\n{random_int}")

    np.random.seed(seed=13)
    random_float = np.random.uniform(low=-1, high=1, size=(2, 3))
    print(f"random float [0.0, 1.0):\n{random_float}")

    fruits = ['🍎', '🍊', '🍌', '🥥', '🍒', '🍍', '🥝', '🍓', '🍑']
    fruit = rng.choice(fruits, size=(3, 3))
    print(f"random fruit:\n{fruit}")

if __name__ == "__main__":
    main()