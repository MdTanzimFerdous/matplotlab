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


# Histogram
def plot13():
    plt.xlabel("Sugar Level")
    plt.ylabel("Number Of Patients")
    plt.title("Blood Sugar Chart")

    blood_sugar_men = [113, 85, 90, 150, 149, 88, 93, 115, 135, 80, 77, 82, 129]
    blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]
    plt.hist([blood_sugar_men, blood_sugar_women], bins=[80, 100, 125, 150], rwidth=0.95, color=['green', 'orange'], label=['men', 'women'])
    plt.legend()
    plt.show()


# Pie
def plot14():
    exp_vals = [1400, 600, 300, 410, 250]
    exp_labels = ["Home Rent", "Food", "Phone/Internet Bill", "Car ", "Other Utilities"]
    plt.axis("equal")
    plt.pie(exp_vals, labels=exp_labels, shadow=True, autopct='%1.1f%%', radius=1.5, explode=[0, 0, 0, 0.1, 0.2], counterclock=True, startangle=45)
    # c:/code/piechart.pdf
    plt.savefig('piechart.png', bbox_inches='tight', pad_inches=2, transparent=True)
    plt.show()


# exercise
def exer():
    company = ['Google', 'AMZN', 'MSFT', 'FB']
    revenue = [90, 136, 89, 27]
    plt.title("US Technology Stocks")
    plt.ylabel('Revenue(Bin)')
    plt.bar(company, revenue)
    plt.savefig("exer.jpg")
    plt.savefig("exer.pdf", pad_inches=5)
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
    plot13()
    plot14()
    exer()


if __name__ == "__main__":
    main()
