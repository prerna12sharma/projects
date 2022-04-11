import random
name=input("enter your name:")
print("HI! ",name,"GLAD TO HAVE YOU ARE HERE")
print("___**WELCOME TO THE GAME-HANGMAN**___")
print("YOU CAN ALSO INVITE YOUR FRIENDS")
def welcome():
    word=["python","ruby","javascript","css","html"]
    x=random.choice(word)
    print(x)
    char=""
    turn=10
    alpha=("abcdefghijklmnopqrstuvwxyz")
    while len(x)>0:
        maxguess=""                                     
        for i in x:
            if i in char:
                maxguess=maxguess+i
            else:
                maxguess=maxguess+"_"
        if maxguess==x:
            if i in char:
                maxguess=maxguess+i
                print("GREAT!,your guess right")
                
            else:
                maxguess=maxguess+"_"
            print(maxguess)
            print("congratulation you are the won")
            break
            
        print(" guess the word",maxguess)
        guess=input("enter your guess:")
        if guess in alpha:
            char=char+guess
            # print(turn,"is left")
        else:
            print("Ooops that letter does not in my word")
            guess=input("enter character")
        if guess not in x:
            # guess=input("enter")
            turn-=1
            # print(turn,"is left")
            # guess=input("enter")
            if turn==9:
                print("9 turn is left!")
                print("---------------")
            if turn==8:
                print("8 turn is left!")
                print("---------------")
                print("       0       ")
            if turn==7:
                print("7 turn is left!")
                print("---------------")
                print("     \0        ")
            if turn==6:
                print("6 turn is left!")
                print("---------------")
                print("      \0/      ")
            if turn==5:
                print("5 turn is left!")
                print("---------------")
            if turn==4:
                print("4 turn is left!") 
                print("---------------")
                print("     \0/       ")
                print("      |        ") 
            if turn==3:
                print("3 turn is left!")
                print("---------------") 
                print("     \0/       ") 
                print("      |        ") 
                print("     /         ")  
            if  turn==2:
                print("2 turn is left!")
                print("---------------")  
                print("     \0/       ") 
                print("      |        ")
                print("     / \       ") 
            if turn==1:
                print("1 turn is left!")  
                print("---------------")
                print("       |       ") 
                print("      \0/      ")
                print("       |       ")
                print("      / \      ")
            if turn==0:
                print("Oops! you have run out")
                print("-----------------")
                print("       |    |   ")
                print("       0    |  ")
                print("      /|\   |  ")
                print("      / \   |  ")
                break
welcome()
        
                
        