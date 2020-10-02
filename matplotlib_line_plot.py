from matplotlib import pyplot as plt
import pandas as pd


data = pd.read_csv('data.csv')

# print(data)

plt.plot(data['Age'], data['Python'], label='Python')
# plt.plot(data['Age'], data['JavaScript'], label='JavaScript')
plt.plot(data['Age'], data['All_Devs'], linestyle='--', label='All_Devs')

overall_median = 57287

# plt.fill_between(data['Age'], data['Python'], alpha=0.25)
# plt.fill_between(data['Age'], data['Python'], overall_median, alpha=0.25)
# plt.fill_between(data['Age'], data['Python'], overall_median, where=(data['Python'] > overall_median),
#                  interpolate=True, alpha=0.25)

# plt.fill_between(data['Age'], data['Python'], overall_median, where=(data['Python'] < overall_median),
#                  interpolate=True, alpha=0.25, color='red')

plt.fill_between(data['Age'], data['Python'], data['All_Devs'], where=(data['Python'] > data['All_Devs']),
                 interpolate=True, alpha=0.25, label='Above Avg')

plt.fill_between(data['Age'], data['Python'], data['All_Devs'], where=(data['Python'] < data['All_Devs']),
                 interpolate=True, alpha=0.25, color='red', label='Below Avg')

plt.legend()

plt.title('Salary by Age in Languanges')
plt.xlabel('Ages')
plt.ylabel('Median Salary')

plt.tight_layout()

plt.show()
