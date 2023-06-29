
# 10.Write a Python program to check if a number is an Armstrong number.\


number = int(input("Enter a number: "))

sum = 0

temp = number

while temp > 0:
    digit = temp % 10
    sum = sum + digit**3
    temp = temp//10

if sum == number:
    print("Armstrong Number")
else:
    print("Not Armstrong number")
