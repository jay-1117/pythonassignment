#17.Write a Python program to count the occurrences of each word in a given sentence


sentence = input("Enter a sentence: ")

words = sentence.split()

Counts = {}

for i in words:
    if i in Counts:
        Counts[i] = Counts[i] + 1
    else:
        Counts[i] = 1


for word, count in Counts.items():
    print(f"'{word}': {count}")
    
