import random
import string
import sys

def string_generator(size=6, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))

department = input("Enter Department: ")  
    
for _ in department:
    
    if department == "Marketing" or department.lower() == "marketing" :
        break
    elif department == "Accounting" or department.lower() == "accounting" :
        break
    elif department == "FinOps" or department.lower() == "finops" :
        break
    else:
        print("Error: You can not use this generator, enter the name correctly.")
        raise SystemExit
        sys.exit()  

number = int(input("Enter the number of EC2 instances required: "))

if number < 0:
    print("Please enter a positive number: ")

elif number > 0:
    print()

print("##########################")
print("   EC2 Instance Names  ")
print("##########################")
print()


for _ in range(1, number + 1):
    unique_name = department
    EC2_unique_name = unique_name + "-" + string_generator()
    print("Your EC2 Instance's unique name is: ", EC2_unique_name)