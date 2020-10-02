from matplotlib import pyplot as plt
import pandas as pd
import statistics


plt.style.use('fivethirtyeight')

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]


data = pd.read_csv('data.csv')
# print(data)
ids = data['Responder_id']
ages = data['Age']
median_age = statistics.median(ages)
# print(f'len: {len(ages)} sum: {sum(ages)} avg: {sum(ages)/len(ages)} median: {median_age}')


bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=bins, edgecolor='black', label="Age Groups", log=True)

plt.axvline(median_age, color="#fc4f30", label='Age Median')

plt.title('Age of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.legend()

plt.tight_layout()

plt.show()
