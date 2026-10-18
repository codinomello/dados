import numpy as np

def main():
    array_row = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    print(f"original row array:\n{array_row}\n")
    array_col = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
    print(f"original column array:\n{array_col}\n")
    
    print(f"{array_row.shape}")
    print(f"{array_col.shape}")

    print(f"multiplication table:\n{array_row * array_col}")

if __name__ == "__main__":
    main()