# Simple function

def greet():
    print("Hello, Monika")

greet()


# with args with return

def sum(num1, num2):
    return num1+num2

result = sum(1,2)

print(result)


# find maximum

numbers = [1,2,3,4,5]

def find_max(numbers):
    largest = numbers[0]

    for n in numbers:
        if n > largest:
            largest = n
    return largest

res = find_max(numbers)
print(res)


# Check Prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print(is_prime(13))


