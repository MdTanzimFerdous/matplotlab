import matplotlib.pyplot as plt
import numpy as np


# Different types of plot
def plot1(x, y):
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.plot(x, y, color="g")
    plt.show()


def plot2(x, y):
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.plot(x, y, 'g+-.')
    plt.show()


def plot3(x, y):
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.plot(x, y, color="g", linewidth=5, linestyle="dotted")
    plt.show()


def plot4(x, y):
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.plot(x, y, color='green', marker='+', linestyle='', markersize=20)
    plt.show()


def plot5(x, y):
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.plot(x, y, color='green', alpha=0.2)
    plt.show()


# Axes Labels, Legend, Grid
def plot6(x, y):
    days = [1, 2, 3, 4, 5, 6, 7]
    max_t = [50, 51, 52, 48, 47, 49, 46]
    min_t = [43, 42, 40, 44, 33, 35, 37]
    avg_t = [45, 48, 48, 46, 40, 42, 41]

    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.title('Weather')

    plt.plot(days, max_t, label="max")
    plt.plot(days, min_t, label="min")
    plt.plot(days, avg_t, label="average")
    plt.legend()
    plt.show()


def plot7(x, y):
    days = [1, 2, 3, 4, 5, 6, 7]
    max_t = [50, 51, 52, 48, 47, 49, 46]
    min_t = [43, 42, 40, 44, 33, 35, 37]
    avg_t = [45, 48, 48, 46, 40, 42, 41]

    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.title('Weather')

    plt.plot(days, max_t, label="max")
    plt.plot(days, min_t, label="min")
    plt.plot(days, avg_t, label="average")
    plt.legend(loc="upper right")
    plt.show()


def plot8(x, y):
    days = [1, 2, 3, 4, 5, 6, 7]
    max_t = [50, 51, 52, 48, 47, 49, 46]
    min_t = [43, 42, 40, 44, 33, 35, 37]
    avg_t = [45, 48, 48, 46, 40, 42, 41]

    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.title('Weather')

    plt.plot(days, max_t, label="max")
    plt.plot(days, min_t, label="min")
    plt.plot(days, avg_t, label="average")
    plt.legend(loc="best")
    plt.show()


def plot9(x, y):
    days = [1, 2, 3, 4, 5, 6, 7]
    max_t = [50, 51, 52, 48, 47, 49, 46]
    min_t = [43, 42, 40, 44, 33, 35, 37]
    avg_t = [45, 48, 48, 46, 40, 42, 41]

    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.title('Weather')

    plt.plot(days, max_t, label="max")
    plt.plot(days, min_t, label="min")
    plt.plot(days, avg_t, label="average")
    plt.legend(loc="best")
    plt.grid()
    plt.show()


# Bar chart
def plot10():
    company = ['GOOGL', 'AMZN', 'MSFT', 'FB']
    revenue = [90, 136, 89, 27]
    ypos = np.arange(len(company))
    plt.xticks(ypos, company)
    plt.xlabel("US Tech Stocks")
    plt.ylabel("revenue")
    plt.bar(ypos, revenue, label="Revenue")
    plt.legend()
    plt.show()


def plot11():
    company = ['GOOGL', 'AMZN', 'MSFT', 'FB']
    revenue = [90, 136, 89, 27]
    profit = [40, 2, 34, 12]
    ypos = np.arange(len(company))
    plt.xticks(ypos, company)
    plt.xlabel("US Tech Stocks")
    plt.ylabel("revenue")
    plt.bar(ypos-0.2, revenue, width=0.4, label="Revenue")
    plt.bar(ypos+0.2, profit, width=0.4, label="Profit")
    plt.legend()
    plt.show()


def plot12():
    company = ['GOOGL', 'AMZN', 'MSFT', 'FB']
    revenue = [90, 136, 89, 27]
    profit = [40, 2, 34, 12]
    ypos = np.arange(len(company))
    plt.xticks(ypos, company)
    plt.xlabel("US Tech Stocks")
    plt.ylabel("revenue")
    plt.barh(ypos-0.2, revenue, height=0.4, label="Revenue")
    plt.barh(ypos+0.2, profit, height=0.4, label="Profit")
    plt.legend()
    plt.show()


def main():
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [50, 51, 52, 48, 47, 49, 46]
    # plt.scatter(x, y, color="m", marker="o", s=30)
    plot1(x, y)
    plot2(x, y)
    plot3(x, y)
    plot4(x, y)
    plot5(x, y)
    plot6(x, y)
    plot7(x, y)
    plot8(x, y)
    plot9(x, y)
    plot10()
    plot11()
    plot12()


if __name__ == "__main__":
    main()
