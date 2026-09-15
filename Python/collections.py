# Find sum of list

numbers = [1,2,3,4,5]

tot = 0

for n in numbers:
    tot+=n

print(tot)

# find largest number

numbers = [1,2,3,4,5]

largest = 0

for n in numbers:
    if n > largest:
        largest = n

print(f"Largest number is {largest}")


# Remove Duplicates

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = set(numbers)

print(unique)

# Store User info

user = {
    "name":"Alice",
    "age":30,
    "city":"Pune"
}

print(user["name"])