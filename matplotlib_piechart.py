from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# slices = [120, 80, 30, 20]
# labels = ['Sixty', 'Forty', 'Thirty', 'Twenty']
# colors = ['blue', 'red', 'yellow', 'green']
# colors = ['#008fd5','#fc4f30', '#e5ae37', '#6d904f']

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]  # 0.1 means 10 percent of the radius


# plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})

'''
autopct: for showing percentage
explode: show pie piece apart from the radius with a percent
shadow: makes it kind of 3d
wedgeprops: style of delimiters between pie pieces
'''

plt.pie(slices, labels=labels, explode=explode, shadow=True, autopct='%1.1f%%',
        wedgeprops={'edgecolor': 'black'})


plt.title('My Pie Chart')
plt.tight_layout()
plt.show()
