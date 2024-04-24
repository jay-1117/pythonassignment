'''22.• Write a Python function to reverses a string if its length is a multiple of
4'''
def checkstr(char):

    if len(char) % 4 == 0:
        return char[::-1]
    else:
        return char


a=input("enter the string:")
str=checkstr(a)
print(str)

