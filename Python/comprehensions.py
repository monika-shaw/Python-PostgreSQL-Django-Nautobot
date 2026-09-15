# Create Squares

squares =[]

for i in range(1,6):
    squares.append(i*i)
print(squares)

# even numbers

even_numbers = []

for i in range(1,11):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)

# convert string to uppercase

names = ["monika", "alice", "jack"]
upper_names = []
for name in names:
    upper_names.append(name.upper())

print(upper_names)


# Dictionary Comprehensions

numbers = [1, 2, 3, 4, 5]

squares = {number: number * number for number in numbers}

print(squares)