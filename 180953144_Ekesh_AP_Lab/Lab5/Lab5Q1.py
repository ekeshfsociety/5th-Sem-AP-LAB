def readData():
    e_id = int(input("Enter Employee ID:"))
    e_name = input("Enter Employee name:")
    e_salary = int(input("Enter Employee salary:"))
    e_department = input("Enter Employee department:")
    return (e_id, e_name, e_salary, e_department)

def searchTuples(id, key):
    for x in id:
        if key in x:
            print("Employee Found:",x)
            return
    print("Employee Not Found")

n = int(input("Number of employees you want to enter:"))
list = []
for i in range(n):
    a = readData()
    list.append(a)

searchkey = int(input("Enter the employee ID of the employee to be searched:"))
searchTuples(list, searchkey)

