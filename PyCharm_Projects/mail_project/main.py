
names_list = []
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.read()
    for name in names.split("\n"):
        names_list.append(name)

mail_content = ""
with open("./Input/Letters/starting_letter.txt", mode='r') as starting_letter_file:
    mail_content = starting_letter_file.read()

for name in names_list:
    new_content = mail_content.replace("[name],", f"{name},")
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt","w") as invite_letter:
        invite_letter.write(new_content)
