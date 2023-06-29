# 5. Write a Python program to check if a number is prime or not

number = int(input("Enter a Number: "))

prime = False
for i in range(2, number//2):
    if number % i == 0:
        prime = True
        break

if prime:
    print("Not prime Number")
else:
    print("prime number")
   