#Accept a list of input from the user until getting value

number = []
while True:
    user_input = input("Enter a value (press Enter to Finish): ")
    if user_input == "":
        break
    else:
        item=number.append(float(user_input))

print("User List: ", number)