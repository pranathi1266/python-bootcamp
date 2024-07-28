#check whether how many vowels in a string
'''str=input()
count=0
vo=['a','e','i','o','u']
print(str.lower())
for i in str:
    if i in vo:
        count+=1
print(count)'''#hlo hi
#            2
'''check=['a','e','i','o','u']
count=0
srt="hellO world"
print(str.lower())
for i in str:
    if(i in check):
        count+=1
print(count)'''
#write a to print all the consonants
'''abc="bcdfghjklmnpqrstvwxyz"
count=0
i="hellO world"
inp=i.lower()
for i in inp:
    if(i in abc):
        count+=1
print(count)'''
##both vowels and consonants
''''check=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
count=0
count1=0
i="hellO world"
inp=i.lower()
for i in inp:
    if(i in check):
        count+=1
print(count)
for i in inp:
    if(i in abc):
        count1+=1
print(count1)'''


#write a to print all the vowels and consonants not the count but string

'''check=['a','e','i','o','u']
abc="bcdfghjklmnpqrstvwxyz"
ans=""
ans1=""
i="hellO world"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=i
print(ans)
for i in inp:
    if(i in abc):
        ans1+=i
print(ans1)'''
'''n=input()
n1=(n.lower())
vowel=0
consonanat=0
vowels=['a','e','i','o','u']
consonanats="bcdfghjklmnpqrstvwxyz"
for i in n1:
    if i in vowels:
        vowel+=1
    elif i in consonanats:
        consonanat+=1
print(consonanat)
print(vowel)'''
        
#write a to print all the vowels followed by consonants
'''n=input()
n1=(n.lower())
x=""
vo=0
v0=['a','e','i','o','u']
con="bcdfghjklmnpqrstvwxyz"
for i in n1:
    if i in con:
        x+=i
print(x)'''
#print the non repeating char in a string
'''v0=['a','e','i','o','u']
con="bcdfghjklmnpqrstvwxyz"
ans=""
i="hello world"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans+=i
print(ans)'''#helo wrd
#add digits in the string
'''str=input()
v0=['a','e','i','o','u']
con="bcdfghjklmnpqrstvwxyz"
digits=['0','1','2','3','4','5','6','7','8','9']
ans=0
for i in str:
    if i in digits:
        ans+=int(i)
print(ans)'''#hello world123
#          6

#add digits in the string using ascii values-48 to 58
'''str=input()
sum=0
for i in str:
    if ord(i)>=48 and ord(i)<=58:
        sum+=int(i)
print(sum)'''#hello world123
#            6
#lowercase letter count
'''str=input()
count=0
for i in str:
    if ord(i)>=97 and ord(i)<=122:
        count+=1
print(count)'''#Hello World123     
#                8
#uppercase letter count
'''str=input()
count=0
for i in str:
    if ord(i)>=65 and ord(i)<=90:
        count+=1
print(count)'''
#uppercase letter letter
'''str=input()
s=""
for i in str:
    if ord(i)>=65 and ord(i)<=90:
        s+=i
print(s)'''
#remove all braces in string
'''str=input()
x="(),[],{}"
str1=""
for i in str:
    if i not in x:
        str1+=i
print(str1)'''#[]23*;
#          23*;
'''str=input()
for i in str:
    if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93 or ord(i)==125 or ord(i)==127):
        pass
    else:
        print(i,end=" ")#[]23*;()
                        #2 3 * ;'''
#if a is input e should be print 4th letter
'''str=input()
for i in str:
     x=ord(i)+4#print()
     y=chr(x)
     print(y,end="")'''#it will work up to u but not for vwxyz
#input:hello---wor--ld
#output:-----helloworld
'''n=input()
res=""
count=0
for i in n:
    if i=='-':
        count+=1
print(count)
for i in n:
    if ord(i)>=97 and ord(i)<=123:
        res+=i
print('-'*count+res)'''
#hello---wor--ld
#5
#-----helloworld
#i=row
#j=col
#1.5
#*****
#*****
#*****
#*****
#*****
'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print("*",end="")
    print()'''
#2.5
#******
#******
#******
#******
#******
'''n=int(input())
for i in range(0,n):
    for j in range(0,n+1):
        print("*",end="")
    print()'''
#3.5
#***
#*
#**
#**
#*
#***
    
'''n=int(input())
for i in range(1,n):
    for j in range(1,n):
        if i==j:
            print( )
        else:
            print("*",end="")
    print()'''
#4.5
# ****
#*  ***
#**  **
#***  *
#****
'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            print(" ",end=" ")
        else:
            print("*",end="")
    print()'''
 # 5
#11111
#22222
#33333
#44444
#55555
'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print(i+1,end="")
    print()'''
 #   5
#12345
#12345
#12345
#12345
#12345
'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        print(j+1,end="")
    print()'''
#5
#1****
#*2***
#**3**
#***4*
#****5
'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            print("*",end="")
        else:
            print(i+1,end="")
    print()'''
#  5
#*2345
#1*345
#12*45
#123*5
#1234*
'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            print(j+1,end="")
        else:
            print("*",end="")
    print()'''
# 5
#*
#**
#***
#****
#*****
'''n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()'''
'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if j<=i:
            print("*",end="")
        else:
            print(" ",end=" ")
    print()'''
'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if(i==j or i>j):
            print("*",end="")
    print()'''
# 5
#*****
#****
#***
#**
#*
'''n=int(input())
for i in range(n,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()'''
'''n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if(i==j or i<j):
            print("*",end="")
    print()'''
    
#5
#*****
#  ****
#    ***
#      **
#        *    
#print upper and lower triangular
#print rhombus and prallogram
#5
# *****
#  *****
#   *****
#    *****
#     *****

'''num=int(input())
for i in range(0, num):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(0, num):
        print("*", end="")
    print()'''

