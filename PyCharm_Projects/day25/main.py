import pandas as pd
import csv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    squirrel_df = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    fur_color = squirrel_df['Primary Fur Color'].value_counts()
    newdf = pd.DataFrame({"Fur Color": fur_color.index, "Count": fur_color.values})
    newdf.to_csv("squirrel_count.csv")




    # df = pd.read_csv('weather_data.csv')
    # # print(df['temp'])
    # # my_dict = dict()
    # my_dict = df.to_dict()
    #
    # # print(my_dict)
    #
    # # temp_list = df['temp'].tolist()
    # #
    # # print(sum(temp_list)/len(temp_list))
    # #
    # # print(df['temp'].mean())
    # # max_temp = df["temp"].max()
    # # print(f"max_temp: {max_temp}")
    #
    # # print(df[df["day"] == "Monday"])
    #
    # # max_temp = df['temp'].max()
    # #
    # # # print(df[df['temp'] == max_temp]["day"])
    # #
    # # # print(df[df.temp == max_temp].day)
    # #
    # # temp_celc = int(df[df.day == "Monday"].temp)
    # # # print(int(temp_celc))
    # # temp_fahr = temp_celc * 1.8 + 32
    # # print(temp_fahr)
    #
    # data_dict = {
    #     "students": ['Onder', "Nihan", "Ali"],
    #     "scores": [76, 56, 65]
    # }
    #
    # # print(data_dict["students"][0])
    # df = pd.DataFrame(data_dict)
    # print(df)
    # df.to_csv("results.csv", sep=";", index_label='Index')
    # # print(df.scores.max())