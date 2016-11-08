'''
#1
g="Hello Will"
print (g)
print(g[0],g[1],g[2])
print (g[-1])
print (g[0:3])
print (g[4:7])
print (g[:4])
print (g[4:])
print (g[:])


#2
a="Hello"
b="World"
print (a+b)
print (a+' '+b)


#3
a="Hello World"
len_a=len(a)
for i in range (0, len_a):
    print (a[i], end="-")
print()
for i in a:
    print (i, end="-")


#4
f_name=input("Enter your first name: ")
l_name=input("Enter your last name: ")
username=f_name[0]+l_name
print(username)


#5
sample=["January", "February", "March", "April","May","June","July","August","September","October","November","December"]
len_s=len(sample)
output=[]
for i in range (0, len_s):
    mid_output=list(sample[i])
    print(mid_output)
    output=output+mid_output[0:3]
    print(output)
print(''.join(output))

jan="January"
feb="February"
mar="March"
apr="April"
may="May"
jun="June"
jul="July"
aug="August"
sep="September"
octo="October"
nov="November"
dec="December"
months=[jan[0:3],feb[0:3],mar[0:3],apr[0:3],may[0:3],jun[0:3],jul[0:3],aug[0:3],sep[0:3],octo[0:3],nov[0:3],dec[0:3]]
print(''.join(months))


#6, #7
jan="January"
feb="February"
mar="March"
apr="April"
may="May"
jun="June"
jul="July"
aug="August"
sep="September"
octo="October"
nov="November"
dec="December"
months=[jan[0:3],feb[0:3],mar[0:3],apr[0:3],may[0:3],jun[0:3],jul[0:3],aug[0:3],sep[0:3],octo[0:3],nov[0:3],dec[0:3]]
complete_month=''.join(months)
user_month_s=int(input("Enter the month number: "))
user_month=complete_month[(user_month_s-1)*3:(user_month_s-1)*3+3]
print(user_month)


#8

sample=input("Enter a string: ")
for i in sample:
    sample_unicode=ord(i)
    print(sample_unicode,end=' ')

for x in range (33,257):
    print(x, ' is ', chr(x) )


#9
a="hello world!"
print (a.capitalize())
print(a.title())
print(a.lower())
print(a.upper())
print(a.replace("e","a"))
print(a.find("e"))


#10
a="Hello {0} {1} world. {2} you.".format("World!","Bye", "Ola!")
print(a)


#11
datestr='Hello .World'
random1, random2, random3=datestr.split("o")
print(random1)
print(random2)
print(random3)


#12
a="   Hello!   "
print(a.strip())


#13
import time
a=open("test_file.txt",'r')

b=a.readline()
i=0
while b:
    time.sleep(1)
    print (i, '-', b)
    b=a.readline()
    i+=1
a.close()


#14
import random

a=open("test_file.txt",'w')
for i in range (0,100):
    a.write(str(random.randint(1,10000))+'\n')
a.close()

b=open("test_file.txt",'r')
d=0
e=0
for i in b:
    c=int(i)
    e=e+c
    print(d, '-', e)
    d+=1
b.close()


#15
file_name=input("Enter the file name: ")
output_file_name=input("Enter the output file name: ")
input_file=open(file_name, 'r')
output_file=open(output_file_name, 'w')
uname=0
for a in input_file:
    f_name, s_name=a.split(' ')
    uname=(f_name[0]+s_name).lower()
    print(uname, file=output_file)
input_file.close()
output_file.close()

'''






    
    
