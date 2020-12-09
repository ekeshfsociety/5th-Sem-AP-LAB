n = int(input("Enter number of elements:"))

c=0

odd_length=0

list_string=[]

odd_length_string=[]

for i in range(0,n):
    list_string.append(input("Enter the string value:"))
    if len(list_string[i])%2 != 0 :
        odd_length+=1
        odd_length_string.append(list_string[i])

for i in range(0,n):
    if list_string[i][0] ==list_string[i][-1]  and len(list_string[i]) >= 2 :
        c+=1
print("The Number of Strings with same First and Last Character are:",c)
print("The Number of Strings with odd length are:",odd_length)
print("The Strings with Odd Length are :",odd_length_string)