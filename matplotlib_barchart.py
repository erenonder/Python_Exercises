import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

dev_age = []
for age in range(25, 36):
    dev_age.append(age)

x_indexes = np.arange(len(dev_age))
width = 0.25

dev_salary = [38496, 42000, 46752, 49320, 53200,
              56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(x_indexes - width, dev_salary, width=width, color='#444444', label='All Devs')

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

plt.bar(x_indexes, py_dev_y, width=width, color='#008fd5', label='Python')


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_indexes + width, js_dev_y, width=width, color='#e5ae38', label='JavaScript')


plt.legend()
plt.xticks(ticks=x_indexes, labels=dev_age)

plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Salary by Age')

plt.tight_layout()

plt.show()
