#Accept a list of 5 float numbers as an input from the user

number = []

for i in range(0,5):
    print("Enter number at localtion ", i, ":")
    item = float(input())
    number.append(item)

print("User List: ", number)