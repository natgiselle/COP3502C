# Write a program called letters.py that counts the number of times a letter appears in a word. The user will enter:
# The word (all lowercase)
# The letter to count (also lowercase)

word = input("Enter a word: ")
letter = input("Enter the letter to count: ")
count=0
for chr in word:
    if chr == letter:
        count+=1

print(f"{letter} appears {count} times.")