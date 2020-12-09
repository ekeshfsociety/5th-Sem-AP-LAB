import string

sentence = input("Enter a sentence:")
finalsentence = sentence.strip()
dict={}
dict['.']=1

for i in finalsentence :
    if i in string.whitespace :
        dict['.'] += 1
print(dict['.'])