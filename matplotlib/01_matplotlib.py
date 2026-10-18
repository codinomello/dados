import matplotlib.pyplot as plt
import numpy as np

def main():
    x1 = np.array([2020, 2021, 2022, 2024, 2025])
    y1 = np.array([6, 8, 6, 5, 7])

    plt.plot(x1,
        y1,
        marker='.',
        markersize=25,
        markerfacecolor="black",
        markeredgecolor="None",
        markeredgewidth=2,
        linestyle="solid",
        linewidth=2,
        color="red",
    )

    x2= np.array([2020, 2021, 2022, 2024, 2025])
    y2 = np.array([4, 6, 9, 7, 10])

    line_style = dict(marker='.',
        markersize=25,
        markerfacecolor="black",
        markeredgecolor="None",
        markeredgewidth=2,
        linewidth=2
    )

    plt.plot(x2, y2, color="green", linestyle="dashed", **line_style)

    x3= np.array([2020, 2021, 2022, 2024, 2025])
    y3 = np.array([9, 5, 4, 9, 7])

    plt.plot(x3, y3, color="blue", linestyle="dashdot", **line_style)

    plt.show()

if __name__ == "__main__":
    main()