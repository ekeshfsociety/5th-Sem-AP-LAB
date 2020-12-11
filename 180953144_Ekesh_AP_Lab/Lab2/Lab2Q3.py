import random

n=int(input("Enter number of elements:"))
dict={}
user_input= int(input("Enter the type of input-> 1:Integer 2:String:"))

if user_input == 1 :
    avg=0
    for i in range(0, n):
        dict[random.randrange(0, 100)] = int(input("Enter a value : "))

    for items in dict.values():
        avg += items

    avg/=len(dict)
    print(avg)

elif user_input == 2 :
    concat_string = ""
    found=False

    for i in range(0, n):
        dict[random.randrange(0, 100)] = input("Enter a value : ")
    search_element = input("Enter the element to search:")

    for items in dict.values():
        special_characters=True
        concat_string+=items
        for ch in items:
            if ch.isalnum():
                special_characters=False
        if special_characters :
            print(items)
        if items == search_element:
            found=True

    print("Concatination:",concat_string)
    print("Element Found:",found)