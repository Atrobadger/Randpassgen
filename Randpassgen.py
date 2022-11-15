import random

charArray = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h',
             'I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p',
             'Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x',
             'Y','y','Z','z','0','1','2','3','4','5','6','7','8','9','!','@',
             '#','$','%','^','&','*','.']

passwordLength = input("Enter a number for password length: ")
passwordSize = int(passwordLength)
arrayLength = len(charArray)
password = ''

for i in range(0, passwordSize):
    randNumber = random.randint(0, arrayLength-1)
    randChar = charArray[randNumber]
    password = password + randChar
print("The generated password is " + password)
