# 7. Write a Python program to check if a number is a power of two.

number = int(input("Enter a Number: "))

flag = False

for i in range(1,number):
    pov = (2**i)
    if pov <= number and pov == number:
        flag = True
        break

if flag:
    print("Power of Two")
else:
    print("not a power of two")


    