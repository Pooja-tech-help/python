str = input("enter a string : ")
rev = ''
for i in str:
    rev = i  + rev
if(str == rev):
    print("string is palindrome")
else:
    print("string is not a palindrome")
