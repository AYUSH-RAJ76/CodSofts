import random

length = int(input("Enter the length of Password: "))
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallchar = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
specialchar = "!@#$%&?"

ratio1 = length//3
ratio2 = length %3

def passwordgenrator(length):
    password = ""
    for i  in range(ratio1):
    
        password += char[random.randint(0,25)]
        password += smallchar[random.randint(0,25)]
        password += nums[random.randint(0,9)]
    
    for i in range(ratio2):
        password += specialchar[random.randint(0,7)]

    return password

_password = passwordgenrator(length)
print("Your Genrated Is :",_password)