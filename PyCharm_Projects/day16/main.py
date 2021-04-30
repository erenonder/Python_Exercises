# from turtle import Turtle, Screen
from prettytable import PrettyTable

my_table = PrettyTable()

my_table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
my_table.add_row(["Adelaide", 1295, 1158259, 600.5])
my_table.add_row(["Brisbane", 5905, 1857594, 1146.4])
my_table.add_row(["Darwin", 112, 120900, 1714.7])
my_table.add_row(["Hobart", 1357, 205556, 619.5])
my_table.add_row(["Sydney", 2058, 4336374, 1214.8])
my_table.add_row(["Melbourne", 1566, 3806092, 646.9])
my_table.add_row(["Perth", 5386, 1554769, 869.4])

my_table.align = "c"

print(my_table)


# x = PrettyTable()
#
# x.add_column("City name",
# ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
# x.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
# x.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
# 1554769])
# x.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
# 869.4])
#
# print(x)


# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()