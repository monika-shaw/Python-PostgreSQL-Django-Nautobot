#Positive, negative or 0
num = int(input("Enter a number "))

if num > 0:
    print("+ve")
elif num < 0:
    print("-ve")
else:
    print("0")

# Even or Odd
num = int(input("Enter a number"))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#Find largest of two number

num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

if num1 > num2:
    print("num1 is largest")
else:
    print(f"{num2} is largest")


# Find largest of three numbers
num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))
num3 = int(input("Enter 3rd number"))

if num1 >= num2 and num1 >= num3:
    print("num1 is largest")
elif num2 >= num1 and num2 >= num3:
    print("num2 is largest")
else:
    print(f"{num3} is largest")
