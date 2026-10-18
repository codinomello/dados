import numpy as np

def main():
    array = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ])
    print(f"original array:\n{array}")

    # array[start:end:step, start:end:step]
    array_slice = array[1:3, 0:4:2]
    print(f"original array:\n{array}")
    print(f"sliced array:\n{array_slice}")

if __name__ == "__main__":
    main()