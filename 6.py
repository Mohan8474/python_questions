#6. Write a Python program to find the missing number in a given list of consecutive numbers.

list1 = [1,2,3,4,6,7,8,10,11]
diff = list1[1]-list1[0]
start = list1[0]
end = list1[-1]

for i in range(start, end, diff):
    if i not in list1:
        print(i)