#Program 1: Check whether a number is even or odd
num = int(input("Enter a number"))

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


check_even_odd(num)

#Program 5: Find factorial of a number
num = int(input("Enter a number"))

def find_fact(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact
res = find_fact(num)
print(res)

#Program 15: Print Fibonacci series

n = 7

a=0
b =1

for i in range(n):
    print(a, end="")
    a, b=b, a+b


#Program 14: Check whether a number is prime

n = 17

if n<2:
    print("Not prime")

for i in range(1,n):
    if n%i ==0:
        print("not pime")
        break
    else:
        print("prime")

#Program 16: Find largest element in a list

numbers = [10, 25, 5, 40, 15]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print(largest)



#Program 17: Remove duplicates from a list

numbers = [10, 25, 5, 40, 15, 15]

unique = list(set(numbers))

print(unique)



#Program 18: Find duplicate elements in a list

numbers = [1, 2, 3, 2, 4, 1, 5]

duplicate=[]

for num in numbers:
    if numbers.count(num) >1  and num not in duplicate:
        duplicate.append(num)

print(duplicate)

