import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.array([2020, 2021, 2022, 2024, 2025])
    y1 = np.array([6, 8, 6, 5, 7])
    y2 = np.array([4, 6, 9, 7, 10])
    y3 = np.array([9, 5, 4, 9, 7])  

    plt.title("class size",
        fontsize=16,
        fontweight="bold",
        family="DejaVu Sans",
        color="black",
    )

    plt.xlabel("year",
        fontsize=14,
        fontweight="bold",
        family="DejaVu Sans",
        color="black",
    )

    plt.ylabel("number of students",
        fontsize=14,
        fontweight="bold",
        family="DejaVu Sans",
        color="black",
    )

    plt.plot(x, y1, label="class A")
    plt.plot(x, y2, label="class B")
    plt.plot(x, y3, label="class C")

    plt.xticks(x, fontsize=12, fontweight="bold", family="DejaVu Sans", color="black")

    plt.show()

if __name__ == "__main__":
    main()