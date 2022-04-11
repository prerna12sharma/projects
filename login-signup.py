import os
import json
print("WELCOME TO LOGIN-SIGNUP")
print("1.signup/2.login")
user=input("enter what u want")
if user=="1":
    name=input("enter your name")
    password1=input("enter your password")
    upper=0
    lower=0
    digit=0
    for i in password1:
        if i.isupper():
            upper=1
        if i.islower():
            lower=1
        if i.isdigit():
            digit=1
        if "@" in password1 or "#" in password1 or "$" in password1 or "&" in password1:
            spcl=1
    total=upper+lower+digit+spcl
    if total!=4:
        print("password should contain only one upper,lower,digit,splc character")
    else:
        password2=input("confirm your password")
        if password1 !=password2:
            print("your password are not same")
        elif password1==password2:
            print("congratulation! you have signin succesfully")
            print("plz make your profile:")
            DOB=input("enter your DOB:")
            gender=input("enter gender:")
            email=input("enter your email:")
            contact=input("enter your contact number:")
            if len(contact)>=0 and len(contact)<=10:
                BIO=input("enter your bio ")
                dict1={}
                dict2={}
                dict3={}
                dict4={}
                dict5={}
                dict6={}
                dict7={}
                dict8={}
                dict={}
                list=[]
                dict1["name"]=name
                dict2["password"]=password1
                dict3["birth date"]=DOB
                dict4["gender"]=gender
                dict5["email"]=email
                dict6["contact"]=contact
                dict7["BIO"] =BIO
                dict8.update(dict1)
                dict8.update(dict2)
                dict8.update(dict3)
                dict8.update(dict4)
                dict8.update(dict5)
                dict8.update(dict6)
                dict8.update(dict7)
                dict["profile"]=dict8
                list.append(dict)
                with open("login-signup.json","w") as file:
                    json.dump(list,file,indent=0)
                print("you have signed up succesfiully")
if user=="2":
    name=input("enter your name")
    password=input("enter your password")
    with open("login-signup.json","r") as file:
        a=file.read()
        if name in a:
            print("your name is already exist")
        else:
            print("plz make your profile:")
            DOB=input("enter your DOB:")
            gender=input("enter gender:")
            email=input("enter your email:")
            contact=input("enter your contact number:")
            if len(contact)>=0 and len(contact)<=10:
                BIO=input("enter your bio ")
                dict1={}
                dict2={}
                dict3={}
                dict4={}
                dict5={}
                dict6={}
                dict7={}
                dict8={}
                list=[]
                dict1["name"]=name
                dict2["password"]=password
                dict3["birth date"]=DOB
                dict4["gender"]=gender
                dict5["email"]=email
                dict6["contact"]=contact
                dict7["BIO"] =BIO
                dict8={}
                dict8.update(dict1)
                dict8.update(dict2)
                dict8.update(dict3)
                dict8.update(dict4)
                dict8.update(dict5)
                dict8.update(dict6)
                dict8.update(dict7)
                list.append(dict8)
                with open("login-signup.json","w") as file:
                    json.dump(list,file,indent=0)
                print("you have login succesfully")
            
            
                              
                
                
            
        