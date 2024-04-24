'''19.Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged '''

char=input("enter the string:")


if len(char)>=3:
   
    if char[-3:]=="ing":
        print(char+"ly")
    else:
        print(char+"ing")    

else:
   print(char)
    
    
print("Modified string:", char)


    
    
