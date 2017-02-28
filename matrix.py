def sum(matrix1,matrix2):
    for i in range (m1):
        for j in range (n1):
            print(matrix1[i][j]+matrix2[i][j],end=' ')
        print()

def product(matrix1,matrix2):
    for i in range (m1):
        for j in range (m1):
            s=0
            for k in range (n1):
                s+=matrix1[i][k]*matrix2[k][j]
            print(s,end=' ')
        print()
                


import random
print("Matrix 1")
print("Enter m:",end='')
m1 = input()
if m1=='-1':
    print("Bye")
    quit()
while not m1.isdigit():
    print("Cannot! Try again.")
    print("Enter m:",end='')
    m1=input()
    if m1=='-1':
        print("Bye")
        quit()
print("Enter n:",end='')
n1 = input()
if n1=='-1':
    print("Bye")
    quit()
while not n1.isdigit():
    print("Cannot! Try again.")
    print("Enter n:",end='')
    n1=input()
    if n1=='-1':
        print("Bye")
        quit()

print("Matrix 2")
print("Enter m:",end='')
m2= input()
if m2=='-1':
    print("Bye")
    quit()
while not m2.isdigit() or (m2!=n1 and m2!=m1):
    print("Cannot! Try again.")
    print("Enter m:",end='')
    m2=input()
    if m2=='-1':
        print("Bye")
        quit()
print("Enter n:",end='')
n2 = input()
if n2=='-1':
    print("Bye")
    quit()
while not n2.isdigit() or not ((n2==n1 and m2==m1) or (n2==m1 and m2==n1)):
    print("Cannot! Try again.")
    print("Enter n:",end='')
    n2=input()
    if n2=='-1':
        print("Bye")
        quit()
n1=int(n1)
m1=int(m1)
matrix1=[[] for i in range (m1)]
for i in range (m1):
    for j in range (n1):
        matrix1[i].append(random.randrange(20))
n2=int(n2)
m2=int(m2)
matrix2=[[] for i in range (m2)]
for i in range (m2):
    for j in range (n2):
        matrix2[i].append(random.randrange(20))
print("Matrix 1")
for i in range (m1):
    for j in range (n1):
        print(matrix1[i][j],end=' ')
    print()
print("Matrix 2")
for i in range (m2):
    for j in range (n2):
        print(matrix2[i][j],end=' ')
    print()
print("Sum")
if n1==n2 and m2==m1:
    sum(matrix1,matrix2)
else:
    print("NA")
print("Product")
if n1==m2 and m1==n2:
    product(matrix1,matrix2)
else:
    print("NA")
