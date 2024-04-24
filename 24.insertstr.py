'''24.• Write a Python function to insert a string in the middle of a string.'''

def insertstr(currstr,newstr):
    middleIndex = len(currstr)

    
    string = currstr[:middleIndex] + newstr + currstr[middleIndex:]
    return string
   
a="hello this is python language "
b="c language"

s=insertstr(a,b)
print(s)


