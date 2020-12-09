list1=[1,2,3,4,5,6,7,8,9,10];
list2=[11,12,13,14,15,16,17,18,19,20];

list3=[]

for i in list1 :
    if i%2 != 0 :
        list3.append(i)

for i in list2:
    if i%2 == 0 :
        list3.append(i)

print(list3)