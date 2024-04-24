#8. Write a Python program to test whether a passed letter is a vowel or
#not.

vowels=['a','e','i','o','u','A','E','I','O','U']

char=str(input("enter the character:",))

if char in vowels:
      print("char is vowels")
else:
    print("char is consonant")
