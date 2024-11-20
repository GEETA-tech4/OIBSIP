import string
import random

length = int (input("Enter Password length:"))

print()

characterList = ""

print("choose charater types to include in the password:")
print("1:Letters (A-Z,a-z)")
print("2:Digit (0-9)")
print("3:Punctuation(Special Characters)")
print("4:Generate password")
# you should be enter only digit value upto 1-4 so our 4 choices are run
while(True):
    try:
        choice = int(input("Pick a no:"))
        if(choice==1):
            characterList += string.ascii_letters
        elif(choice == 2):
            characterList +=string.digits
        elif(choice==3):
            characterList += string.punctuation
        elif(choice==4):
            if characterList:
               break
            else:
                print("Please Pick A valid option please!!!")
    except ValueError:
         print("Invalid input! Please enter a number between 1 and 4.")

password = []

for i in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)

print("The random password is" + "".join(password))
