from turtle import Turtle, Screen
import pandas as pd


turtle = Turtle()

states_df = pd.read_csv("50_states.csv")

states_list = states_df['state'].tolist()
# print(states_list)

guessed_states_list = list()
states_to_learn = set()


screen = Screen()

screen.setup(width=800, height=600)
screen.title(titlestring="States Game")

screen.bgpic("blank_states_img.gif")
game_on = True
mistake_count = 0

turtle.hideturtle()
turtle.penup()
state_correct = 0
while game_on:
    guessed_state_name = screen.textinput(title=f"{state_correct}/50 Guessed", prompt="State Name:").title()

    if guessed_state_name == "Exit":
        print("Exiting game")
        states_to_learn = set(states_list) - set(guessed_states_list)
        print(states_to_learn)
        game_on = False
    elif guessed_state_name in states_list and guessed_state_name not in guessed_states_list:
        x_corr = int(states_df[states_df['state'] == guessed_state_name].x)
        y_corr = int(states_df[states_df['state'] == guessed_state_name].y)
        turtle.setposition(x=x_corr, y=y_corr)
        turtle.write(guessed_state_name, move=False, align="center", font=("Arial", 8, "normal"))
        state_correct += 1
        guessed_states_list.append(guessed_state_name)
    elif guessed_state_name in guessed_states_list:
        print("You already guessed this state")
    else:
        print(f"There is no such state named {guessed_state_name}")
        mistake_count += 1

    if mistake_count >= 3:
        game_on = False
        states_to_learn = set(states_list) - set(guessed_states_list)
        print("Game over")


df_states_to_learn = pd.DataFrame(states_to_learn, columns=['States To Learn'])
df_states_to_learn.to_csv("states_to_learn.csv", index=False)


screen.exitonclick()



