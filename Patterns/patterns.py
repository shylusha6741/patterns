
# 12
# 123
# 1234
# 12345
for j in range(1,6,1):
    for i in range(1,j+1,1):
        print(i,end="")
    print()


# 1
# 22
# 333
# 4444
# 55555

for j in range(1,6,1):
    for i in range(1,j+1,1):
        print(j,end="")
    print()

# 5
# 44
# 333
# 2222
# 11111

for j in range(5,0,-1):
    for i in range(5,j-1,-1):
        print(j,end="")
    print()

#     1
#    22
#   333
#  4444
# 55555

for j in range(1,6,1):
    for s in range(5,j,-1):
        print(" ",end="")
    for i in range(1,j+1,1):
        print(j,end="")
    print()

# 55555
#  4444
#   333
#    22
#     1

for j in range(5,0,-1):
    for s in range(5,j,-1):
        print(" ",end="")
    for i in range(j,0,-1):
        print(j,end="")
    print()

#     1
#    222
#   33333
#  4444444
# 555555555
for j in range(1,6,1):
    for s in range(4,j,-1):
        print(" ",end="")
    for i in range(j,0,-1):
        print(j,end="")
    for k in range(2,j+1,1):
        print(j,end="")
    print()


# 1
# 21
# 321
# 4321
# 54321
for j in range(1,6,1):
    for i in range(j,0,-1):
        print(i, end="")
    print()

# 5
# 54
# 543
# 5432
# 54321
for j in range(5,0,-1):
    for i in range(5,j-1,-1):
        print(i,end="")
    print()


# 5
# 45
# 345
# 2345
# 12345
for j in range(5,0,-1):
    for i in range(j,6,1):
        print(i, end="")
    print()
# 12345
# 1234
# 123
# 12
# 1
for j in range(5,0,-1):
    for i in range(1,j+1,1):
        print(i,end="")
    print()

# 1
# 22
# 333
# 4444
# 55555
for j in range(1,6,1):
    for i in range(1,j+1,1):
        print(j,end="")
    print()

# 54321
# 4321
# 321
# 21
# 1
for j in range(5,0,-1):
    for i in range(j,0,-1):
        print(i,end="")
    print()
#      1
#     12
#    123
#   1234
#  12345
for j in range(1,6,1):
    for s in range(5,j-1,-1):
        print(" ",end="")
    for i in range(1,j+1,1):
            print(i,end="")
    print()

#     5
#    54
#   543
#  5432
# 54321
for j in range(5,0,-1):
    for s in range(1,j,1):
        print(" ",end="")
    for i in range(5,j-1,-1):
        print(i,end="")
    print()
# 12345
#  1234
#   123
#    12
#     1
for j in range(5,0,-1):
    for s in range(5,j,-1):
        print(" ",end="")
    for i in range(1,j+1,1):
        print(i,end="")
    print()
#     1
#    212
#   32123
#  4321234
# 543212345
for j in range(1,6,1):
    for s in range(5,j,-1):
        print(" ",end="")
    for i in range(j,0,-1):
        print(i,end="")
    for k in range(2,j+1,1):
        print(k,end="")
    print()


#     *
#    ***
#   *****
#  *******
# *********   
for j in range(1,6,1):
    for s in range(5,j,-1):
        print(" ",end="")
    for i in range(j,0,-1):
        print("*",end="")
    for k in range(2,j+1,1):
        print("*",end="")
    print()

#  123454321
#   2345432
#    34543
#     454
#      5
for j in range(1,6,1):
    for s in range(1,j+1,1):
        print(" ",end="")
    for i in range(j,6,1):
        print(i,end="")
    for k in range(4,j-1,-1):
        print(k,end="")
    print()



for j in range(1,6,1):
    for i in range(5,j,-1):
        print(" ",end="")
    for i in range(1,j+1,1):
        print(i,end="")
    for k in range(j-1,0,-1):
        print(k,end="")
    print()

# 543212345
#  5432345
#   54345
#    545
#     5  
for j in range(1,6,1):
    for s in range(1,j,1):
        print(" ",end="")
    for i in range(5,j-1,-1):
        print(i,end="")
    for k in range(j+1,6,1):
        print(k,end="")
    print()

# *****
# 12345
# 12345
# 12345
# 12345
for j in range(1,6,1):
    for i in range(1,6,1):
        if(j==1):
            print("*",end="")
        else:
            print(i,end="")
    print()
# *****
# 12345
# *****
# 12345
# *****
for j in range(1,6,1):
    for i in range(1,6,1):
        if(j==1 or j==3 or j==5):
            print("*",end="")
        else:
            print(i,end="")
    print()

# * * *
# * * *
# * * *
# * * *
# * * *
for j in range(1,6,1):
    for i in range(1,6,1):
        if(i==1 or i==3 or i==5):
            print("*",end="")
        else:
            print(" ",end="")
    print()

#   *  
#   *  
# *****
#   *  
#   *  
for j in range(1,6,1):
    for i in range(1,6,1):
        if(i==3 or j==3):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# *******
# *     *
# *     *
# *     *
# *     *
# *     *
# *******
for j in range(1,8,1):
    for i in range(1,8,1):
        if(i==1 or i==7 or j==1 or j==7):
            print("*",end="")
        else:
            print(" ",end="")
    print()
# *******
# *  *  *
# *  *  *
# *******
# *  *  *
# *  *  *
# *******
for j in range(1,8,1):
    for i in range(1,8,1):
        if(i==1 or i==7 or i==4 or j==1 or j==7 or j==4):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# ****   
#    *   
#    *   
#    *   
#    *   
#    *   
#    * 
for j in range(1,8,1):
    for i in range(1,8,1):
        if(j==1 and i<=4 or i==4):
            print("*",end="")
        else:
            print(" ",end="")
    print()
# ****   
#    *   
#    *   
#    *   
#    *   
#    *   
#    ****
for j in range(1,8,1):
    for i in range(1,8,1):
        if(j==1 and i<=4 or i==4 or j==7 and i>=4):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# ****  *
#    *  *
#    *  *
# *******
# *  *   
# *  *   
# *  ****
for j in range(1,8,1):
    for i in range(1,8,1):
        if(j==1 and i<=4 or i==4 or j==7 and i>=4 or j==4 or i==1 and j>=4 or i==7 and j<=4):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# *    
#  *   
#   *  
#    * 
#     *
for j in range(1,6,1):
    for i in range(1,6,1):
        # if(i==1 and j==1 or i==2 and j==2 or i==3 and j==3 or i==4 and j==4 or i==5 and j==5):
        if i==j:
            print("*",end="")
        else:
            print(" ",end="")
    print()






# *     *
#  *   * 
#   * *  
#    *   
#    *   
#    *   
#    * 
for j in range(1,8,1):
    for i in range(1,8,1):
        if(i==j and j<=4 or i==4 and j>=4 or i+j==8 and j<=4):
             print("*",end="")
        else:
            print(" ",end="")
    print()

# *  ****
# *  *   
# *  *   
# *******
#    *  *
#    *  *
# ****  *
for j in range(1,8,1):
    for i in range(1,8,1):
        if(i==1 and j<=4 or j==1 and i>=4 or i==4 or j==4 or j==7 and i<=4 or i==7 and j>=4):
            print("*",end="")
        else:
            print(" ",end="")
    print()



        