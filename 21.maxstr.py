'''21.Write a Python function that takes a list of words and returns the length
of the longest one.'''


def longeststr(char):
    maxstr=0

    for i in char:
        if len(i)>maxstr:
            maxstr=len(i)
    return maxstr

a=["hii","hello","world","cricket"]
print("the longest one is :",longeststr(a)) 
         
