import pandas as pd
df = pd.read_csv('Pandas_Demo/data/survey_results_public.csv')

# print(df.info)
# print(df.head(6))
# print(df.tail(8))
# print(df.shape)
# print(df.iloc[1:4, 3:7])
print(df['Hobbyist'].value_counts())
