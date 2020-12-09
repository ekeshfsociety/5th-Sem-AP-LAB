#Lab 3 Q2

def unique(list):
	uniquelist = [] 
	
	for i in list:
		if i not in uniquelist:
			uniquelist.append(i)
	
	return uniquelist

n = int(input("Enter the number of elements : "))
list = []

for i in range(n):
	list.append(int(input("Enter element : ")))
	
print("List of unique elements")
print(unique(list))