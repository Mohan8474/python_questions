# Write a Python program to find the first non-repeating element in a list
list1 = [1,2,4,2,5,6,8,3,5,8,1]
for i in list1:
    if list1.count(i) == 1:
        print(i)
        break