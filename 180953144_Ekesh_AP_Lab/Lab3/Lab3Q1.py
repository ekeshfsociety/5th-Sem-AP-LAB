def multiply_all_numbers(list):
    m=1
    
    for i in list:
        if i == 0:
            return 0
        m = m * i
    return m

n=int(input("Enter number of elements:"))

list = []
 
for i in range(n):
    list.append(int(input("Enter element:")))

print("Multiplication:",multiply_all_numbers(list))