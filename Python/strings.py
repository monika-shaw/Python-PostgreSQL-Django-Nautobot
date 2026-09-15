# print and access string
my_string = "Hello, world!"

print(my_string)
print(my_string[0])
print(my_string[-1])
print(my_string[::-1])


# Reverse a string
my_name = "Monika"

reversed = my_name[::-1]
print(reversed)

#count characters
characters = "abcdef"

print(len(characters))

#count vowels

alphabets = "Programming in Python"

count = 0

for c in alphabets:
    if c in "aeiou":
        count+=1

print(count)


# check Pallindrome

my_str = input("Enter a string")

reversed_str = my_str[::-1]

if(my_str == reversed_str):
    print("Pallindrome")
else:
    print("Not a Pallindrome")