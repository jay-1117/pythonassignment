'''23.Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.'''

#held
def addstr(str):
     if len(str) < 2:
        return ""
     else:
        string = str[:2] + str[-2:]
        return string
        
    
a="helloworld"

s=addstr(a)
print("before:",a)
print("after:",s)




