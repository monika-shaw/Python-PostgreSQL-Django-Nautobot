#Program 31: Read a text file
with open("data.txt","r") as file:
    content = file.read()

# print(content)


#Program 32: Write data into a file

text = "I am software dev"

with open("data.txt", "w") as file:
    file.write(text)

print("File written")