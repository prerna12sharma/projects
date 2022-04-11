import random
digit=5
name=input("enter your name:")
print("________",name,"_______")
print("_______________________")
print("__welcome to cowbull__")
print("______________________")
def getsecretnum():
    num=list(range(10))
    random.shuffle(num)
    return num
def cluies():
    num1=getsecretnum()
    list=[]
    for i in range(digit):
        list.append(num1[i])
    return list
def check_num():
    cow=[]
    bull=[]
    num2=cluies()
    i=0
    maxguess=10
    print(num2)
    while maxguess>0:
        guess=int(input("enter guess num"))
        pos=int(input("enter your pos num"))
        if guess in num2:
            index=num2.index(guess)
            if index==pos:
                if guess not in bull:
                    bull.insert(index,guess)
                    print("bull",bull)
                else:
                    print("plz try to different digit")
            elif index!=pos:
                cow.append(guess)
                print("cow",cow)
            else:
                print("this num does not exist list")
        if bull==num2:
            print(name,"congratulation")
            break
        maxguess-=1
        print(maxguess,"turn is left")
    else:
        ("u run out!","u loose the game")
    return bull
# check_num()
def play_again():
    while True:
        again=input("u want to play again yes or not")
        if again=="yes":
            check_num()
        else:
            break
play_again()
    
    