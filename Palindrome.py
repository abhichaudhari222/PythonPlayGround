check=input("Enter String or Number to check: \n")
if check==check[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")