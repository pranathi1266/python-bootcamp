#6.take a space seperated input from auser and print alternate elements
'''l1=list(map(int,input().split()))
for  i in range(0,len(l1),2):
    print(l1[i],end=" ")'''
#7you are given with a comma seperated naturals nums 1-10 print only even nums 
'''l1=list(map(int,input().split(",")))
for i in range(1,len(l1),2):
    print(l1[i])'''

'''l1=list(map(int,input().split(",")))
for i in range(1,len(l1)+1,1):
    if (i%2==0):
        print(i)'''

#8 you r given a space seperated  integer list find no.of even elements and no.of odd elements in a list
'''l1=list(map(int,input().split(",")))
even_count=0
odd_count=0
for i in range(len(l1)):
    if (l1[i]%2==0):
       even_count+=1
    else:
       odd_count+=1
print(even_count, odd_count)'''
#9 take a space seperated find the avg of ele in the even indexs
'''l1=list(map(int,input().split(",")))
sum=0
n=len(l1)
count=0
for i in range(len(l1)):
    sum+=l1[i]
    count+=1
print(sum/count)'''
'''l1=cc
even=0
avg=0
count=0
for i in range(len(l1)):
    if(i%2==0):
        count+=1
        even+=l1[i]
        avg=even/count
print(even)
print(avg)'''






    
    