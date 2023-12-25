# celsius_temps = [0, 10, 20, 30, 40]

# def hi(x):
#     print((x * 9/5) + 32)

# hi(50)
# # Convert Celsius to Fahrenheit using a lambda function
# fahrenheit_temps = list(map(lambda x: (x * 9/5) + 32, celsius_temps))
# print(fahrenheit_temps)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def n(x):
#     return x%2==0

# # Filter even numbers using a lambda function
# even_numbers = list(filter(n, numbers))
# print(even_numbers)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # Filter even numbers using a lambda function
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# books = [
#     {'title': '1984', 'author': 'George Orwell'},
#     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
#     {'title': 'Brave New World', 'author': 'Aldous Huxley'}
# ]

# # Sort books by title using a lambda function
# sorted_books = sorted(books, key=lambda x: x['title'])
# print(sorted_books)

# words = ['apple', 'banana', 'orange', 'grape', 'kiwi']
# sorted_words = sorted(words, key=lambda x: len(x))
# print(sorted_words)

# prices = [100, 200, 300, 400, 500]

# discounted_prices = list(map(lambda x: x * 0.9, prices))
# print(discounted_prices)

# books = [
#     {'title': '1984', 'author': 'George Orwell'},
#     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
#     {'title': 'Brave New World', 'author': 'Aldous Huxley'}
# ]
# sorted_books = sorted(books, key=lambda x: (len(x['title']), x['title']))
# print(sorted_books)


# def sum(a,b):
#     return (a+b)
# a=10
# b=20
# print(lambda a,b: a+b)

# def x(a):
#     return a+10
# print(x(5))
# def x(a):
#     print(a+2)
# x(10)
# x = lambda a: print(a+2)
# x(10)


