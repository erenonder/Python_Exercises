from matplotlib import pyplot as plt
import numpy as np
import os
import pandas as pd
from collections import Counter
import csv

plt.style.use('fivethirtyeight')

data = pd.read_csv('/Users/ondereren/Downloads/data.csv')
# print(data)

ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

languages = []
popularity = []


for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title('Most Popular Languages')
plt.xlabel('Number of People Who Use')
# plt.ylabel('Programming Languages')
plt.tight_layout()
plt.show()