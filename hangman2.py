import random
name=input("enter your name")
print("HI!__",name,"GLAD TO HAVE YOU ARE HERE")
print("WELCOME TO THE HANGMAN GAME")
print("YOU CAN ALSO INVITE YOUR FRIENDS")
def welcome():
    list=["python","ruby","css","html","javascript"]
    x=random.choice(list)
    return x
def game_run():
    alpha=("abcdefghijklmnopqrstuvwxyz h ")
    word=welcome()
    li=[]
    turn=8
    guessed=""
    while len(word)>0:
        guess=input("enter your guess")
        print("you have",turn,"is left")
        if len(guess)==1:
            if guess not in alpha:
                print("make sure you enter a alpjabet not a num")
            elif guess in li:
                print("you have already entered this char")
            elif guess not in word:
                print("SOORY!,that letter is not a part of list")
                li.append(guess)
                turn-=1
            elif guess in word:
                print("Great!,your guessed word correctly")
            else:
                print("you have enter the wrong char")
        elif len(guess)==len(word):
            if guess ==word:
                print("Great job!you guessed the word correctly")
            else:
                print("sorry! that was not the word")
    else:
        print("the length of your guess is not the lengthn the correct word")
        turn-=1
    string=""
    if guessed==False:
        for i in word:
            if i in li:
                string+=i
            else:
                string="_"
        print(string)
    if string==word:
        print("Great job! your guessed is correct")
    if guessed==True:
        turn-=1
    elif turn==0:
        print("oops!you are run out")
game_run()   
        
                
        
    
    
    
                    