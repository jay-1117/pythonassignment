#16.Write a Python program to count occurrences of a substring in a string


string = input("Enter a string: ")
substring = input("Enter a substring to count: ")

count = string.count(substring)
print(f"The substring '{substring}' appears {count} time(s) in the string.")
    
