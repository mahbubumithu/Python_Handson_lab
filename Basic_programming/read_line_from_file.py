# Open the file in read mode
with open("test.txt", "r") as file:
    # Read all lines into a list
    lines = file.readlines()

    # Check if the file has at least 4 lines
    print(lines[3].strip())  # line[3] because indexing starts from 0
    