#14.Write a Python program to count the number of characters (character frequency) in a string

char=str(input("Enter the string:"))

freq={}

for i in char:
    if char in freq:
        freq[char]= freq[char]+1

    else:
        freq[char]=1

for char, count in freq.items():
    print("Character '{}' appears {} time(s) in the string.".format(char, count))       
