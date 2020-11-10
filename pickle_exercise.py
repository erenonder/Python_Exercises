
import pickle

saved_list = [i if i % 2 == 0 else i**2 for i in range(0, 10)]

saved_tuple = (0, 1, 2, 3)

# print(saved_tuple)

with open('onder_pickle.txt', 'wb') as file:

    pickle.dump(saved_list, file)
    pickle.dump(saved_tuple, file)


with open('onder_pickle.txt', 'rb') as file:
    retrieved_list = pickle.load(file)
    retrieved_tuple = pickle.load(file)

print(retrieved_list)
print(retrieved_tuple)
