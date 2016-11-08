'''
#1
def header_file():
    print("Hello and welcome!!!")
    print("Don't get lost!")

header_file()


#2
def mean(a,b,c,d):
    sum=a+b+c+d
    print ("Mean of four numbers: ", sum/4)
a=2
b=3
c=4
d=5
mean(a,b,c,d)


#3
def reverse_string():
    text=input("What's your string?")
    text_list=list(text)
    print (text_list)
    text_len=int(len(text_list))
    temp=0
    for i in range (0,text_len//2):
        temp=text_list[i]
        text_list[i]=text_list[text_len-i-1]
        text_list[text_len-i-1]=temp
    print(text_list)
    print(''.join(text_list))

reverse_string()


#4
def biodata():
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    address=input("Enter your address: ")
    state=input("Enter your state: ")
    zipcode=input("Enter your zipcode: ")

    print(name, " aged ", age, " years, lives at ", address, state, zipcode)

biodata()


#5
def friends():
    friends_names={"One":"1","Two":"2", "Three":"3", "Four":"4", "Five":"5"}
    print (friends_names.keys())

friends()


#6
def total_amt(amount, tax):
    total=amount+(tax*amount/100)
    return total

amount=int(input("Enter the amount: "))
tax=int(input("Enter the tax: "))
total_amount=total_amt(amount, tax)
print("The total bill is: ", total_amount)


#7
def powers(a,b,c):
    total=a**(b**c)
    return total

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
total=powers(a,b,c)
print("The value of a^b^c is ", total)


#8
def quarters():
    q=int(input("Number of quarters: "))
    qinp=q*25
    return qinp

def dimes():
    d=int(input("Number of dimes: "))
    dinp=d*10
    return dinp

def nickels():
    n=int(input("Number of nickels: "))
    ninp=n*5
    return ninp

def pennies():
    p=int(input("Number of pennies: "))
    return p

total_amt=(quarters()+dimes()+nickels()+pennies())/100
print("The total dollar value is: ", total_amt)


#9
import math
def shape():
    user_shape=input("Shape you want: ")
    return user_shape

def rectangle(a,b):
    area_r=a*b
    return area_r

def triangle(b,h):
    area_t=0.5*b*h
    return area_t

def circle(r):
    area_c=math.pi*r*r
    return area_c

user_shape=shape()
if user_shape=="rectangle":
    a=int(input("Enter length of rectangle: "))
    b=int(input("Enter width of rectangle: "))
    print("Area of the rectangle is: ", rectangle(a,b))

elif user_shape=="triangle":
    b=int(input("Enter the length of base of triangle: "))
    h=int(input("Enter the height of the triangle: "))
    print("Area of triangle is: ", triangle(b,h))

elif user_shape=="circle":
    r=int(input("Enter the radius: "))
    print("Area of circle is: ", circle(r))

else:
    print("Invalid shape")


#10
import random
def random_num():
    list_var=[]
    for i in range(0,5):
        list_var.append(random.randint(1,20))
    print(list_var)

random_num()


#11
import random
import time
def random_dec():
    for i in range (1,15):
        print(random.random())
        time.sleep(3)

random_dec()


#12
def biodata():
    name=input("Enter your name: ")
    age=input("Enter your age: ")
    address=input("Enter your address: ")
    state=input("Enter your state: ")
    zipcode=input("Enter your zipcode: ")
    print("Name: ", name)
    print("Age: ", age)
    print("Address: ", address)
    print("State: ", state)
    print("Zipcode: ", zipcode)

biodata()



#TicTacToe - Attempt I


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
'''

#TicTacToe - Attempt II

#TicTacToe
import sys
def board():
    for i in range (1,10,3):
        if i==4 or i==7:
            print()
        print (i,":", slate[i], "|", i+1, ":", slate[i+1],"|",i+2,":",slate[i+2])
    print()

def player():
    player1x=int(input("Player 1 - Choose a number between 1 - 9: "))
    while player1x in player_attempts:
        print ("Invalid number: Try Again!")
        player1x=int(input("Player 1 - Choose a number between 1 - 9: "))
    slate[player1x]="x"
    player_attempts.append(player1x)
    
def win(var):
    if (slate[1]==var and slate[2]==var and slate[3]==var):
        print("Player ",var," Wins!")
        sys.exit()
    elif (slate[1]==var and slate[5]==var and slate[9]==var):
        print("Player ",var," Wins!")
        sys.exit()
    elif (slate[1]==var and slate[4]==var and slate[7]==var):
        print("Player ",var," Wins!")
        sys.exit()
    elif (slate[4]==var and slate[5]==var and slate[6]==var):
        print("Player ",var," Wins!")
        sys.exit()
    elif (slate[7]==var and slate[8]==var and slate[9]==var):
        print("Player ",var," Wins!")
        sys.exit()
    elif (slate[2]==var and slate[5]==var and slate[8]==var):
        print("Player ",var," Wins!")
        sys.exit()
    elif (slate[3]==var and slate[6]==var and slate[9]==var):
        print("Player ",var," Wins!")
        sys.exit()
    elif (slate[1]==var and slate[5]==var and slate[9]==var):
        print("Player ",var," Wins!")
        sys.exit()
    
slate={1:'_', 2:'_', 3:'_', 4:'_', 5:'_', 6:'_', 7:'_', 8:'_', 9:'_'}
player_attempts=[]

board()

for a in range (1,10):
    player1x=int(input("Player 1 - Choose a number between 1 - 9: "))
    while player1x in player_attempts:
        print ("Invalid number: Try Again!")
        player1x=int(input("Player 1 - Choose a number between 1 - 9: "))
    slate[player1x]="x"
    player_attempts.append(player1x)
    board()
    win("x")
    
    player2o=int(input("Player 2 - Choose a number between 1 - 9: "))
    while player2o in player_attempts:
        print ("Invalid number: Try Again!")
        player2o=int(input("Player 2 - Choose a number between 1 - 9: "))
    slate[player2o]="o"
    player_attempts.append(player2o)
    board()
    win("o")
