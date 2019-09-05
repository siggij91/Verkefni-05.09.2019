##Design an algorithm that generates the first 
#n numbers in the following sequence:
#; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

#Algorithm:
#From n(4) on, n(x) is the sum of n(x-1), n(x-2), n(x-3)
#Hardcode print of first 3 n depending on input
#If n>3 use while loop to update n(x) and print
#repeat until at n

n = int(input("Enter the length of the sequence: ")) # Do not change this line