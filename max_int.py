## Verkefni 05.09.2019
#Design an algorithm that finds the maximum 
#positive integer input by a user.  The user 
#repeatedly inputs numbers until a negative value is entered.

#Algorithm:
#Take input number and put it in variable
#End program if negative
#Go to while loop if positive and ask for new number
#If negative end program and print
#Put in greatest number variable if greater than greatest number variable and ask for new number 

num_int = int(input("Input a number: "))    # Do not change this line

max_int = num_int

if num_int >= 0:
    
    while num_int >= 0:
        
        num_int = int(input("Input a number: "))
        
        if num_int > max_int:
            max_int = num_int
    
    else:
        print("The maximum is", max_int)    # Do not change this line