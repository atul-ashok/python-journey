
'''
#1
list_names=["A","F","C","D","E"]
print(list_names)

#2
print(len(list_names))

#3
print(list_names[1])

#4
print(list_names[1:4])

#5
list_names[2]="F"
print (list_names)

#6
list_names.insert(2,"G")
print (list_names)

#7
list_names.append("H")
print(list_names)

#8
list_names.pop(3)
print(list_names)

print(list_names.pop(3))
print(list_names)

#9
list_names.remove("B")
print (list_names)

#10
t=list_names.pop(2)
print(list_names)
print (t)

#11
list_names.sort()
list_names_reversed=list_names
print (list_names)
list_names.sort(reverse=True)
print (list_names_reversed)

#12
greeting="Hello How are you string"
print (greeting.split())

print(list(greeting))
greeting1=greeting.split()
print (greeting1)

greeting2="".join(greeting1)
print(greeting2)
greeting3=" ".join(greeting1)
print(greeting3)
greeting4=",".join(greeting1)
print(greeting4)
print(greeting5=":".join(greeting1))

#13, #14, #15
password_list=["Apples123", "Pancakes4ever", "Oliver", " "]
password_list.append("Password")
wrong_password=[]
i=0
while i<=3: #while True:
    user_password=input("Enter your password: ")
    if user_password in password_list:
        print("Access granted")
        break
    else:
        print("Access denied")
        wrong_password.append(user_password)
    i+=1
print('Incorrect Passwords',wrong_password)

#16
import random
random_num=[]
for i in range (1, 20):
    random_num.append(random.randint(1,20))
print(random_num)

#17
import random
cartoon_list=["Atom ant", "Dexter", "T-bone", "Swatkats", "Tom", "Jerry", "Goku", "Gohan", "Piccollo", "Vegeta"]
for num in range (0,10):
    random.shuffle(cartoon_list)
    print(cartoon_list[0])

#18
import random
cartoon_list=["Atom ant", "Dexter", "T-bone", "Swatkats", "Tom", "Jerry", "Goku", "Gohan", "Piccollo", "Vegeta"]
for num in range (0,10):
    print(random.choice(cartoon_list))

#19
print(list("Swat Kats"))

#20
L=["a", "b", "c"]
"c" in L

#21
cartoon_list=["Atom ant", "Dexter", "T-bone", "Swatkats", "Tom", "Jerry", "Goku", "Gohan", "Piccollo", "Vegeta"]
for var in cartoon_list:
    print(var)

greeting="Hello Good Morning"
for var in greeting:
    print(var)
'''

#Lists & Random mini project

import random
fruit_list=["dragon fruit", "mango", "pineapple", "raspberry", "blueberry", "blackberry", "papaya", "custard apple", "kiwi" ,"cranberry", "apple", "orange", "banana", "watermelon", "strawberry", "peach", "musk melon", "grape"]
random_fruit=random.choice(fruit_list)
#print (random_fruit)
len_random_fruit=len(random_fruit)
#print(len_random_fruit)
fruit_name_list=list(random_fruit)
#print(fruit_name_list)
fruit_name1=fruit_name_list[:]
#print (fruit_name1)
blank_fruit=[]
for sample in range (0, len_random_fruit):
    blank_fruit.insert(sample, '_')
print("Guess the fruit to win!!!")
print(blank_fruit)

while blank_fruit!=fruit_name_list: #to check for guessed letter
    user_letter=input("Enter a letter to fill the blank: ")
    if user_letter in fruit_name1:
        letter_pos=fruit_name1.index(user_letter)
        blank_fruit[letter_pos]= user_letter
        fruit_name1[letter_pos]='-'
        print(blank_fruit)
    elif user_letter=="yw": #to provide cheat code
        random_letter=random.choice(fruit_name_list)
        clue_pos=fruit_name1.index(random_letter)
        blank_fruit[clue_pos]=random_letter
        fruit_name1[clue_pos]='-'
        print(blank_fruit)
    else:
        print('Try again')
        
print ('The fruit to guess was: ', random_fruit)
        






















