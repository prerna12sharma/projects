password1=input("enter your password")
if len(password1)>=6 and len(password1)<=12:
    if password1>="A" or password1<="Z" and password1>="a" or password1<="z":
        if password1>="0" and password1<="9" :
            if "@" in password1 or "$" in password1 or "&" in password1:
                print("correct password")
            else:
                print("missing special correcter")
        else:
            print("missing number")
    else:
        print("missing upper case")
else:
    print("you have take password len between 6 to 12")
        
                    