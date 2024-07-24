#password verifier
#mr.x is trying to create a new password for this insta account these are the requried conditions for creating a new password
#con:1 mini length is 8 and max length is 15
#con:2 only @,/ is allowed in a password
#con:3 no spaces are allowed
#con:4 only alpha numerics are allowed
#you r supposed to print weak password is length is exact 8
#medium password if length is b/w 8-12
#strong password if length is b/w 12-15
'''password=input()
str="@,/,/t"
count=0
length=len(password)
print(len(password))
if (len(password)>=8 and len(password)<=15):
    for i in password:
        if i in str[0] or str[1] and str[2]!=i:
            count+=1
    print("acc")
else:
    print("pls follow the conditions")
if(password==8):
    print("password is weak password")
elif (length<8 and length>12):
    print("password is medium password")
else:
    print("password is strong password")'''
    #soring elements in assending and desending
'''l1=list(map(int,input().split( )))
dec=[]
for i in range(len(l1)):
    l1.sort()
print(l1)
for j in range(len(l1),-1,-1,-1):
    dec.append(len(j))
print(l1)'''
#gcd of 2 num##lcm*gcd=a*b
'''a=int(input())
b=int(input())
while b!=0:
    a,b=b,a%b#a=b,b=a%b
print(a)'''
    
#lcm of 2 numbers
 #lcm= a*b%gcd

'''a=int(input())
b=int(input())
c=a*b
while b!=0:
    a,b=b,a%b#a=b,b=a%b
print("gcd is",a)
print("lcm is",c//a)'''
#prime numbers or not
'''n=int(input())
r=int(n**0.55)
for i in range(1,int(n**0.55)+1):
    if (n%i==0):
        print("prime")
        break
    else:
        print("not a prime")'''
'''n=int(input())
r=n**0.5
fact=0
for i in range(2,int(r+1)):
    if (n%i==0):
        fact+=1
        break
    if fact>=1:
        print("not a prime")
    else:
        print("prime")'''
        

#write a program all prime in a given range
'''n=int(input())
m=int(input())
for i in range(n,m+1):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        print(i)'''
#leap year#it should be divisible by 400 or divisible by 4and or for 100
'''n=int(input())
if n%400==0:
    print("leap")
else:
    print("not a leap")'''
'''n=int(input())
if (n%4==0 or n%100!=0):
    print("leap")
else:
    print("not a leap")'''
#leap year in an range
'''n=int(input())
for i in range(2000,2035):
    if n%400==0:
        print("leap")
else:
    print("not a leap")'''
'''y1=int(input())
y2=int(input())
count=0
for i in range(y1,y2+1):
    if i%400==0:
        print(i,"is leap year")
    elif i%4==0 and i%100!=0:
        print(i,"is leap year")
        count+=1

print(count)'''
    
    
    





    


    