m=int(input("Enter rows:"))
n=int(input("Enter columns:"))
p=int(input("Enter rows:"))
q=int(input("Enter columns:"))

#dictionary
d1={}
d2={}
d3={}

#setting values for dictionary
for i in range(m):
    d1[i]={}
for i in range(p):
    d2[i]={}
for i in range(m):
    d3[i]={}

print("Enter First Matrix")
for i in range(0,m):
    for j in range(0,n): 
        val=int(input("Value = "))
        d1[i][j]=val

print("Enter Second Matrix")
for i in range(0,p):
    for j in range(0,q):
        val=int(input("Value = "))
        d2[i][j]=val

for i in range(0,m):
    for j in range(0,n):
        d3[i][j]=d1[i][j]+d2[i][j]
for i in d3.keys():
    if d3.get(i)==0:
        del d[i]
print(d3)