import string 
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

char_numbers = input("How many Characters for the password")

while True:
    try:
        char_numbers = int(char_numbers)
        if char_numbers < 6:
            print("Password must be at least 6 characters")
            char_numbers = input("Please Enter Number again!!")
        else:
            break
    except:
            print("Must be integer Value")
            char_numbers = input("Please Enter Number again!!")


random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(char_numbers * 0.3) 
part2 = round(char_numbers * 0.2)


password = []

for i in range(part1):
     password.append(s1[i])
     password.append(s2[i])

for i in range(part2):
     password.append(s3[i])
     password.append(s4[i])   

random.shuffle(password)

password = ''.join(password[0:])

print(password)