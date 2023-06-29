#2. Write a Python program to generate the Fibonacci sequence up to a given number of terms.


n = int(input("Enter Number: "))

n1 = 0
n2 = 1
count = 0

if n == 0:
    print("Enter number greater than 0")
elif n == 1:
    print(n1)
else:
    while count<n:
        print(n1)
        next_value = n1 + n2
        n1 = n2
        n2 = next_value
        count = count +1