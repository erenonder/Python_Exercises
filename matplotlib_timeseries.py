from matplotlib import pyplot as plt
import pandas as pd
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta


plt.style.use('seaborn')

# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]

# y = [0, 1, 3, 4, 6, 5, 7]

data = pd.read_csv('data.csv')
# print(data)

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

open_val = data['Open']
high_val = data['High']
close_val = data['Close']
dates = data['Date']


plt.plot_date(dates, close_val, linestyle='solid')

plt.gcf().autofmt_xdate()

# date_format = mpl_dates.DateFormatter('%b, %d %Y')

# plt.gca().xaxis.set_major_formatter(date_format)

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Price')

plt.tight_layout()

plt.show()
