height_1=int(input("Enter your Height in inches: "))
height_2=int(input("Enter your Height in inches: "))

avarage_height=(height_1+height_2)/2
print(avarage_height)
feet=int(avarage_height//12)
print(feet)
inche=int(avarage_height%12)
print(inche)
print(f"Print in Human Redable formate: {feet}'{inche}''")
