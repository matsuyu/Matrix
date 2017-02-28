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
invalid = True
while invalid:
    invalid = False
    if m1=='-1':
        print("Bye")
        quit()
    if not m1.isdigit():
        invalid = True
        print("Cannot! Try again.")
        print("Enter m:",end='')
        m1=input()
        continue
    m1 = int(m1)
    if m1<1 or m1>5:
        invalid = True
        print("Cannot! Try again.")
        print("Enter m:",end='')
        m1=input()
        continue
    
print("Enter n:",end='')
n1 = input()
invalid = True
while invalid:
    invalid = False
    if n1=='-1':
        print("Bye")
        quit()
    if not n1.isdigit():
        invalid = True
        print("Cannot! Try again.")
        print("Enter n:",end='')
        n1=input()
        continue
    n1 = int(n1)
    if n1<1 or n1>5:
        invalid = True
        print("Cannot! Try again.")
        print("Enter n:",end='')
        n1=input()
        continue

print("Matrix 2")
print("Enter m:",end='')
m2= input()
invalid = True
while invalid:
    invalid = False
    if m2=='-1':
        print("Bye")
        quit()
    if not m2.isdigit():
        invalid = True
        print("Cannot! Try again.")
        print("Enter m:",end='')
        m2=input()
        continue
    m2 = int(m2)
    if m2<1 or m2>5:
        invalid = True
        print("Cannot! Try again.")
        print("Enter m:",end='')
        m2=input()
        continue
    if m2!=n1 and m2!=m1:
        invalid = True
        print("Cannot! Try again.")
        print("Enter m:",end='')
        m2=input()
        continue
print("Enter n:",end='')
n2 = input()
invalid = True
while invalid:
    invalid = False
    if n2=='-1':
        print("Bye")
        quit()
    if not n2.isdigit():
        invalid = True
        print("Cannot! Try again.")
        print("Enter n:",end='')
        n2=input()
        continue
    n2 = int(n2)
    if n2<1 or n2>5:
        invalid = True
        print("Cannot! Try again.")
        print("Enter n:",end='')
        n2=input()
        continue
    if (not(n1==n2 and m1==m2)) and (not (n1==m2 and m1==n2)):
        invalid = True
        print("Cannot! Try again.")
        print("Enter n:",end='')
        n2=input()
        continue
matrix1=[[] for i in range (m1)]
for i in range (m1):
    for j in range (n1):
        matrix1[i].append(random.randrange(20))
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
