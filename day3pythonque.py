#1.find the elements that is  present in k+n index, k is given by user /k=3//n=2//3 6 8 61 2//o/p-2
'''k=int(input())
n=int(input())
l1=list(map(int,input().split()))
if (len(l1)<k+n):
    print("error")
else:
    for i in range(0,l1[1]):
        sum=k+n
        print(l1[sum])
        break#or you can use exit(0)'''
#2.print the element in a particular index//k=3//1 2 3 4 5 6/o/p :4//k=8//1 2 3 4 5 6 /o/p:3
'''k=int(input())
q=0
l1=list(map(int,input().split()))
for i in range(1,l1[1]+1):
    q=k%len(l1)//
print(l1[q-1])//'''
'''k=20
70 4 5 66 77 45 44 //k=20,7
1  2 3  4  5  6  7//idx 6'''

#3.find the maximum element in a given list//i/p-22 4 55 6 77 87  99//0/p-99///i/p-54 -44 -34 99 44//0/p-99
'''l1=list(map(int,input().split()))
for i in range(1,l1[1]+1):
     for j in range(1,l1[1]+1):
          if(l1[i]<l1[j]):
              max=l1[j]
print(max)'''
'''l1=list(map(int,input().split()))
max=l1[0]
for i in range(len(l1)):
    if(l1[i]>max):
        max=l1[i]
print(max)'''
#4.find the maximum element in a given list
'''l1=list(map(int,input().split()))
min=l1[0]
for i in range(len(l1)):
    if(l1[i]<min):
        min=l1[i]
print(min)'''
#5.replace the element in an array with avg of max and min elements
#13 2 67 20 68
#68+2=70
#70/2=35
#35 35 35 35 35
'''l1=list(map(int,input().split()))
min=l1[0]
max=l1[0]
sum=0
for i in range(len(l1)):
    if(l1[i]<min):
        min=l1[i]   
print(min)
for i in range(len(l1)):
    if(l1[i]>max):
        max=l1[i]
print(max)
sum=min+max #or avg=()
print(sum)
avg=sum//2
print(avg)
for i in range(len(l1)):
    l1[i]=avg
print(l1)'''
#find even or odd
#find greatest of 3
#find sum of all ele in an arr
#find pick element in an arr
#find max ele in an arr
#finf 2nd max ele in an arr
#reverse an arr without using any built in functions
#find the missing num in an arr
#find the sum squares of given number
#find sum of squares of even and odd digits
#check whether the given num  is palindrome or not using while loop
#write a pro to print first n fibinocci series
l1=list(map(int,input().split()))
n=int(input())
x=(n*(n+1))//2
sum=0
for i in range(0,len(l1)):
    sum+=l1[i]
    z=x-sum
print(z)
#find the duplicates in an arr

'''l1=list(map(int,input().split()))
no_dup=[]
for i in l1:
    if (i not in no_dup):
        no_dup.append(i)
print(*no_dup)'''#1 2 3 4 5 5
                # 1 2 3 4 5
