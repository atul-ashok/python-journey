'''
#1
BillMarks=[86,80,78,94]
TomMarks=[65,78,79,87]
MikeMarks=[89,76,87,75]
ClassMarks=[BillMarks, TomMarks, MikeMarks] #Math, Writing, History, Science

#print("Tom scored ",ClassMarks[1][2], "in History")
average_subject=input("Enter the subject for which you would like the average: ")
#total=[sum(l) for l in ClassMarks]
#print (total)
if average_subject=="Math":
    i=0
elif average_subject=="Writing":
    i=1
elif average_subject=="History":
    i=2
elif average_subject=="Science:":
    i=3
else:
    print("Invalid Input!")
sum=0
for a in range (0,3):
    sum=sum+ClassMarks[a][i]

print("Average of the class in ", average_subject, "is ", sum/3)

print (ClassMarks)


#2
family=("Dad", "Mom", "Brother","Brother")
print (family)
print(family.count("Brother"))
print(family.index("Brother"))


#3
import random
select_random=random.randint(20,30)
guess_number=0
i=0
list_guess=[]
while (guess_number!=select_random or i==10):
    guess_number=int(input("Input a number to guess: "))
    list_guess.append(guess_number)
    i+=1
print("The correct value is: ", select_random)
print("Your guessed values are: ", list_guess)
print("Your number of attempts: ", i)


#4, #5, #6, #7
friends={"one":1, "two":2,"three":3, "four":4, "five":5}
print(friends["two"])
print(friends.keys())
print(friends.values())
friends["six"]=6
print(friends)
del friends["one"]
print (friends)


#8
prices={"Rice":2, "Wheat":4, "Flour":6, "Bread":8, "Milk":10}
print (prices)

for key in sorted(prices):
    print (key, prices[key])


#9
prices={"Rice":2, "Wheat":4, "Flour":6, "Bread":8, "Milk":10}
print ("These are the available items: ", prices.keys())
user_select=input("Which item would you like to buy? : ")
if (user_select in prices.keys()):
    print ("This is what it will cost you: ", prices[user_select])
else:
    print ("Try elsewhere")

#10, #11
user_db={"Dad":1, "Mom":2, "Brother":3, "Sister":4}
user_id=input("What is the username?: ")
if (user_id in user_db.keys()):
    user_pwd=int(input("What is the password?: "))
    if (user_pwd == user_db[user_id]):
        print ("Access Granted!")
    else:
        print("Access Denied!")
else:
    print("Invalid ID!")




#Quiz project:

import random
Q1="Question1: "
Q2="Question2: "
Q3="Question3: "
Q4="Question4: "
Q5="Question5: "
q_list=[Q1,Q2,Q3,Q4,Q5]
print(random.shuffle(q_list))
questions={"Q1":"A1", "Q2":"A2", "Q3":"A3", "Q4":"A4", "Q5": "A5"}
print(random.shuffle(questions))



'''
#TicTacToe

slate={1:'_', 2:'_', 3:'_', 4:'_', 5:'_', 6:'_', 7:'_', 8:'_', 9:'_'}
player_attempts=[]

for i in range (1,10,3):
    if i==4 or i==7:
        print()
    print (i,":", slate[i], "|", i+1, ":", slate[i+1],"|",i+2,":",slate[i+2])
print()

for a in range (1,10):
    player1x=int(input("Player 1 - Choose a number between 1 - 9: "))
    while player1x in player_attempts:
        print ("Invalid number: Try Again!")
        player1x=int(input("Player 1 - Choose a number between 1 - 9: "))
    slate[player1x]="x"
    player_attempts.append(player1x)
    for i in range (1,10,3):
        if i==4 or i==7:
            print()
        print (i,":", slate[i], "|", i+1, ":", slate[i+1],"|",i+2,":",slate[i+2])
    print()

    if (slate[1]=="x" and slate[2]=="x" and slate[3]=="x"):
        print("Success")
        break
    elif (slate[1]=="x" and slate[5]=="x" and slate[9]=="x"):
        print("Success")
        break
    elif (slate[1]=="x" and slate[4]=="x" and slate[7]=="x"):
        print("Success")
        break
    elif (slate[4]=="x" and slate[5]=="x" and slate[6]=="x"):
        print("Success")
        break
    elif (slate[7]=="x" and slate[8]=="x" and slate[9]=="x"):
        print("Success")
        break
    elif (slate[2]=="x" and slate[5]=="x" and slate[8]=="x"):
        print("Success")
        break
    elif (slate[3]=="x" and slate[6]=="x" and slate[9]=="x"):
        print("Success")
        break
    elif (slate[1]=="x" and slate[5]=="x" and slate[9]=="x"):
        print("Success")
        break

    player2o=int(input("Player 2 - Choose a number between 1 - 9: "))
    while player2o in player_attempts:
        print ("Invalid number: Try Again!")
        player2o=int(input("Player 2 - Choose a number between 1 - 9: "))
    slate[player2o]="o"
    player_attempts.append(player2o)
    for i in range (1,10,3):
        if i==4 or i==7:
            print()
        print (i,":", slate[i], "|", i+1, ":", slate[i+1],"|",i+2,":",slate[i+2])
    print()

    if (slate[1]=="o" and slate[2]=="o" and slate[3]=="o"):
        print("Success")
        break
    elif (slate[1]=="o" and slate[5]=="o" and slate[9]=="o"):
        print("Success")
        break
    elif (slate[1]=="o" and slate[4]=="o" and slate[7]=="o"):
        print("Success")
        break
    elif (slate[4]=="o" and slate[5]=="o" and slate[6]=="o"):
        print("Success")
        break
    elif (slate[7]=="o" and slate[8]=="o" and slate[9]=="o"):
        print("Success")
        break
    elif (slate[2]=="o" and slate[5]=="o" and slate[8]=="o"):
        print("Success")
        break
    elif (slate[3]=="o" and slate[6]=="o" and slate[9]=="o"):
        print("Success")
        break
    elif (slate[1]=="o" and slate[5]=="o" and slate[9]=="o"):
        print("Success")
        break





















           
