question_list = ["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai"]
options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
solution_list = [3, 4, 1] 
fifty_fifty = [
['1.Four','3.seven'],['2.Bhopal','4.Delhi'],['1.Software Engineering','2.Counseling']]
i = 0
c=0
print("you have 5050 lifeline , if you want you  can  use it by entering '5050' ")
while i < len(question_list):
    print(question_list[i])
    j = 0
    while j < len(options_list[i]):
        print(options_list[i][j])
        j +=1
    user=int(input("enter your number option: "))
    if user == solution_list[i]:
        print('congress')
    elif user == 5050:
        if c == 0:
            print(fifty_fifty[i])
            c+=1
            user1  = int(input("enter your option now : "))
            if user1 == solution_list[i]:
                print("congrates! , you choice correct option" )
            else:
                print("sadly!, your choice wrong option")
        else:
            print("you used fifty fifty ,so please enter your own answer") 
            
    else:
        print("oops! your answer is wrong ")
        print('quite')
        break
