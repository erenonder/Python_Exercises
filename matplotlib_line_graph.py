from matplotlib import pyplot as plt


plt.style.use('fivethirtyeight')

dev_age = []
for age in range(25, 36):
    dev_age.append(age)


dev_salary = [38496, 42000, 46752, 49320, 53200,\
         56000, 62316, 64928, 67317, 68748, 73752]


# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]


plt.plot(dev_age, py_dev_y, label='Python')

plt.plot(dev_age, js_dev_y, label='JavaScript')

plt.plot(dev_age, dev_salary, label='All Devs', color='#444444', marker='.', linestyle='--')

plt.xlabel("Age")
plt.ylabel('Salary')
plt.title('Median Salary by Age')

plt.legend()

# plt.grid(True)

plt.tight_layout()

plt.show()
