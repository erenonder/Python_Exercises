import pandas as pd
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df_nato = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {data.letter: data.code for (index, data) in df_nato.iterrows()}
# print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_code(name_to_code):
    try:
        spell_list = [nato_dict[letter] for letter in name_to_code]
    except KeyError as error_message:
        print("Sorry only letters on the alphabet please!")
    else:
        print(spell_list)

given_name = ""
while given_name != "EXIT":
    given_name = input("Enter a word to spell: ").upper()
    generate_code(given_name)
