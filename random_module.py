# 1. random()
# Generates a random floating-point number between 0 and 1.


# import random

# random_number = random.random()

# print(random_number)

# # 2. randint()
# # Generates a random integer within a specified range.


# import random

# random_int = random.randint(1, 10)  # Generates a random integer between 1 and 10 (inclusive)
# print(random_int)
# # 3. choice()
# # Selects a random element from a sequence.


# import random

# my_list = ['apple', 'banana', 'cherry', 'date']
# random_element = random.choice(my_list)
# print(random_element)
# # 4. shuffle()
# # Randomly shuffles a sequence in place.


# import random 

# my_list = [1, 2, 3, 4, 5]
# random.shuffle(my_list)
# print(my_list)
# # 5. sample()
# # Generates a specified number of unique elements from a sequence without replacement.

# import random

# my_list = ['red', 'green', 'blue', 'yellow', 'orange']
# random_sample = random.sample(my_list, 1)  # Generates 3 unique elements from the list
# print(random_sample)
# # 6. uniform()
# # Generates a random floating-point number within a specified range.


# import random

# random_float = random.uniform(2.5, 5.5)  # Generates a random float between 2.5 and 5.5
# print(random_float)