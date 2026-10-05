#Find the average of numbers from 1 to N.
   # Example: If N = 5, calculate the average of 1, 2, 3, 4, 5.

n=5
sum=0
for i in range(1,n+1,1):
        sum=sum+i
avg=sum/n
print("Average of numbers from 1 to",n,"=",avg)


#2.Find the sum of squares of numbers from 1 to N.
    #Example: If N = 5, calculate 1² + 2² + 3² + 4² + 5².

n=int(input("enter a value:"))
sum=0
for i in range(1,n+1,1):
    squ=i*i
    sum=sum+squ
print(sum)

#3.Find the sum of cubes of numbers from 1 to N.
   # Example: If N = 5, calculate 1³ + 2³ + 3³ + 4³ + 5³.

n=int(input("enter a value: "))
sum=0
for i in range(1,n+1,1):
    cube=i*i*i
    sum=sum+cube
print(sum)

#4.Calculate the power of a number without using the ** operator.
   # Example: If base = 2 and power = 5, calculate 2 × 2 × 2 × 2 × 2.

base=int(input("enter base value: "))
power=int(input("enter power value: "))
result=1
for i in range(1,power+1,1):
    result=result*base
print(result)

#5.Display the first N terms of the Fibonacci series.
    #Example: If N = 7, display 0, 1, 1, 2, 3, 5, 8.

n=int(input("enter a value: "))
a=0
b=1
for i in range(0,n,1):
    print(a, end=" ")
    c=a+b
    a=b
    b=c

#6.Display the first N terms of the series:
    #1, 1/2, 1/3, 1/4, ...
    #Example: If N = 4, display 1, 1/2, 1/3, 1/4.
n=int(input("enter a value: "))
for i in range(1,n+1,1):
    print(f"1/{i}")

# 7.Display the first N terms of the series:
    # 1, 11, 111, 1111, 11111, ...
    # Example: If N = 5, display 1, 11, 111, 1111, 11111.

n=int(input("enter a value: "))
num=0
for i in range(1,n+1,1):
    num=num*10+1
    print(num,end=" ")



#8.Display the first N terms of the series:
    # 1, 3, 9, 27, 81, ...
    # Each term is obtained by multiplying the previous term by 3.

n=int(input("enter the value: "))
num=1
for i in range(1,n+1,1):
    print(num,end=" ")
    num=num*3




for year in range(1,2027,1):
    newnum=year
    rev=0
    while newnum!=0:
         ld=newnum%10
         rev=rev*10+ld
         newnum=newnum//10
    if rev==year:
         print(year)