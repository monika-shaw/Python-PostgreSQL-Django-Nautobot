# Print 1-10
for i in range(1,11):
    print(i)

# Print even numbers

for i in range(1,11):
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")


#Multiplication Table

num = 5

for i in range(1,11):
    table = i * num
    print(table)


# Sum numbers from 1 - 100

tot = 0
for i in range(1,101):
    tot+=i
print(tot)


# Factorial

num = 5

fact = 1
for i in range(1, num+1):
    fact*=i
print(fact)


# while loop

number = 1

while number <=5:
    print(number)
    number+=1