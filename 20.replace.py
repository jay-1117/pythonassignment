'''20. Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.'''

def replace(char):
    
    notindex = char.find('not')
    poorindex = char.find('poor')
    
    if char != -1 and poorindex != -1 and notindex < poorindex:
        return char[:notindex] + 'good' + char[poorindex + 4:]
        
    else:
        return input_string
   
string = input("Enter a string: ")
s = replace(string)
print(s)



