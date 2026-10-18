import numpy as np

def main():
    two_dim_array = np.array([
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I']
    ])
    print(f"two-dimensional (2D) array:\n{two_dim_array}\n")

    print(f"number of dimensions from two-dimensional array: {two_dim_array.ndim}")
    print(f"shape of two-dimensional array: {two_dim_array.shape}")

    two_dim_word = two_dim_array[2, 1] + two_dim_array[2, 2]
    print(f"word formed from 2D array: {two_dim_word}\n")

    three_dim_array = np.array([
        [ 
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['G', 'H', 'I']
        ],
        [
            ['J', 'K', 'L'],
            ['M', 'N', 'O'],
            ['P', 'Q', 'R']
        ],
        [
            ['S', 'T', 'U'],
            ['V', 'W', 'X'],
            ['Y', 'Z', ' ']
        ]
    ])
    print(f"three-dimensional (3D) array:\n{three_dim_array}\n")

    print(f"number of dimensions from three-dimensional array: {three_dim_array.ndim}")
    print(f"shape of three-dimensional array: {three_dim_array.shape}")

    three_dim_word = three_dim_array[0, 0, 0] + three_dim_array[2, 0, 0] + three_dim_array[2, 0, 0]
    print(f"word formed from 3D array: {three_dim_word}")

if __name__ == "__main__":
    main()