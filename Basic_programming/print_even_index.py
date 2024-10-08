data = input("Enter your Characters: ")
size = len(data)

print("Printing Only Even Index Characters: ")
for i in range(0,size-1,2):
    print(data[i])