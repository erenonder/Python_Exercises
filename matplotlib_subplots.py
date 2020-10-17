from matplotlib import pyplot as plt
import pandas as pd


plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
# print(data)

ages = data['Age']
all_salaries = data['All_Devs']
python_salaries = data['Python']
java_salaries = data['JavaScript']


fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)


ax1.plot(ages, all_salaries, label='All', linestyle='--')
ax2.plot(ages, python_salaries, label='Python')
ax2.plot(ages, java_salaries, label='Java')


# ax1.set_xlabel('Age')
ax1.set_ylabel('Salary')

ax2.set_xlabel('Age')
ax2.set_ylabel('Salary')

ax1.legend(loc='upper left')
ax2.legend(loc='upper left')

ax1.set_title('Salaries by Age')
# ax2.set_title('Salaries by Age')

plt.tight_layout()

plt.show()

# fig.savefig('fig.png')