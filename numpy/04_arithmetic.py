import numpy as np

def main():
    array = np.array([
        [1.1, 2.2, 3.3],
        [4.4, 5.5, 6.6],
        [7.7, 8.8, 9.9],
    ])
    print(f"original array:\n{array}\n\n")

    array_add = array + 1
    print(f"array after addition:\n{array_add}\n")
    
    array_sub = array - 2
    print(f"array after subtraction:\n{array_sub}\n")
    
    array_mul = array * 3
    print(f"array after multiplication:\n{array_mul}\n")
    
    array_div = array / 4
    print(f"array after division:\n{array_div}\n")

    array_exp = array ** 5
    print(f"array after exponentiation:\n{array_exp}\n")

    array_mod = array % 6
    print(f"array after modulus:\n{array_mod}\n")

    # vectorized operations
    array_sqrt = np.sqrt(array)
    print(f"array after square root:\n{array_sqrt}\n")
    
    array_log = np.log(array)
    print(f"array after natural logarithm:\n{array_log}\n")

    array_round = np.round(array)
    print(f"array after rounding:\n{array_round}\n")

    array_floor = np.floor(array)
    print(f"array after flooring:\n{array_floor}\n")

    array_ceil = np.ceil(array)
    print(f"array after ceiling:\n{array_ceil}\n")

    radii = np.array([1, 2, 3])
    areas = np.pi * (radii ** 2)
    print(f"areas of circles with given radii:\n{areas}")

    # element-wise operations
    array_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    array_b = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

    array_sum = array_a + array_b
    print(f"\nelement-wise sum of arrays:\n{array_sum}\n")
    
    array_difference = array_b - array_a
    print(f"element-wise difference of arrays:\n{array_difference}\n")
    
    array_product = array_a * array_b
    print(f"element-wise product of arrays:\n{array_product}\n")
    
    array_quotient = array_b / array_a
    print(f"element-wise quotient of arrays:\n{array_quotient}\n")
    
    array_power = array_a ** 2
    print(f"element-wise exponentiation of first array:\n{array_power}\n")

    array_modulus = array_b % array_a
    print(f"element-wise modulus of second array by first array:\n{array_modulus}\n")

    # comparative operations
    print(f"element-wise comparison (array_a < array_b):\n{array_a < array_b}\n")
    print(f"element-wise comparison (array_a <= array_b):\n{array_a <= array_b}\n")
    print(f"element-wise comparison (array_a == array_b):\n{array_a == array_b}\n")
    print(f"element-wise comparison (array_a >= array_b):\n{array_a >= array_b}\n")
    print(f"element-wise comparison (array_a > array_b):\n{array_a > array_b}\n")

if __name__ == "__main__":
    main()