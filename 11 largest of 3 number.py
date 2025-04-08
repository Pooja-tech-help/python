num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))
num3 = int(input("enter 3rd number:"))

if num1 > num2:
    if num1 > num3:
        print(f'largest number is : {num1}')
    else:
        print(f'largest number is : {num3}')
else:
    if num2 > num3:
        print(f'largest number is : {num2}')
    else:
        print(f'largest number is : {num3}')


