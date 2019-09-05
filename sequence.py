##Design an algorithm that generates the first 
#n numbers in the following sequence:
#; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

#Algorithm:
#From n(4) on, n(x) is the sum of n(x-1), n(x-2), n(x-3)
#Hardcode print of first 3 n depending on input
#If n>3 use while loop to update n(x) and print
#repeat until at n

n = int(input("Enter the length of the sequence: ")) # Do not change this line

nx0 = int()
nx_min1 = int()
nx_min2 = int()
nx_min3 = int()

for num in range(1,n+1):
    if num == 1:
        print('1')
        nx_min3 = 1
    elif num == 2:
        print('2')
        nx_min2 = 2
    elif num == 3:
        print('3')
        nx_min1 = 3
    else:
        nx0 = nx_min1 + nx_min2 + nx_min3
        print(str(nx0))
        nx_min3 = nx_min2
        nx_min2 = nx_min1
        nx_min1 = nx0

#Implementation changed from origininal algorithm