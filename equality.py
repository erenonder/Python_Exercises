# equality.py


class Drink():

    def __init__(self, drink_name, alcoholic=False):
        self.drink_name = drink_name
        self.alcoholic = alcoholic

    def __eq__(self, other):
        return self.alcoholic == other.alcoholic


pepsi = Drink('pepsi')
cola = Drink('cola')
beer = Drink('beer', True)

if pepsi == beer:
    print('Both are drinks')

if pepsi is cola:
    print('Both are same')

first_list = [1, 2, 3]
second_list = [1, 2, 3]
third_list = first_list

if first_list == second_list:
    print('Same list')

if first_list is second_list:
    print('Same object')

if first_list is third_list:
    # is keyword compares the output of id() function
    print('first_list and third_list Same object')

third_list[0] = 9
print(first_list)

print(id(first_list))
print(id(third_list))
print(id(second_list))
