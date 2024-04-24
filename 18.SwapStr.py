#18.Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.

char1 = input("Enter the first string: ")
char2 = input("Enter the second string: ")

swapChar1 = char2[:2] + char1[2:]
swapswapChar2 = char1[:2] + char2[2:]

res = swapChar1 + " " + swapChar2
print("String:", res)




