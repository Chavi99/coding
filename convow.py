b=['a','e','i','o','u','A','E','I','O','U']
a=input()
if a>='A' and a<='Z' or a>='a' and a<='z':
    if a in b:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid")
