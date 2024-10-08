def sumof_current_and_previous_number(range_limit):
    previous_number= 0
    for current_number in range(range_limit+1):
        
        sum = current_number + previous_number
        
        print("Current Number {0} Previous Number {1} Sum: {2}" .format(current_number,previous_number,sum))
        previous_number = current_number

range_limit=int(input("Printing Current and Previous Number sum in a Range: "))
print(sumof_current_and_previous_number(range_limit))