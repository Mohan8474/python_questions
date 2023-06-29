# 3. Write a Python program to check if two strings are anagrams.
# (string that contains same characters, only the order of characters can be different)

str1 = input("Enter word 1: ")
str2 = input("Enter Word 2: ")

if len(str1) == len(str2):
    anagram = True
    for i in str1:
        if i in str2:
            pass
        else:
            print("Not anagram")
            anagram = False
            break
    if anagram:
        print("Anagram")
else:
    print("Not anagram")