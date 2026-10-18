import numpy as np

def main():
    array = np.array([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ])
    print(f"mean of array: {np.mean(array)}")
    print(f"sum of array: {np.sum(array)}")
    print(f"standard deviation of array: {np.std(array)}")
    print(f"variance of array: {np.var(array)}")
    print(f"minimum of array: {np.min(array)}")
    print(f"maximum of array: {np.max(array)}")
    print(f"maximum argument of array: {np.argmin(array)}")
    print(f"maximum argument of array: {np.argmax(array)}")

if __name__ == "__main__":
    main()