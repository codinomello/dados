import numpy as np

def main():
    print(f"numpy version: {np.__version__}")

    list = [1, 2, 3, 4, 5]
    print(f"numpy list: {list}")

    array = np.array(list)
    array *= 2
    print(f"numpy array: {array}")

if __name__ == "__main__":
    main()