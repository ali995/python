text = input("your text: ")
dict = {}
for i in range(len(text)):
    key=text[i]
    val=text.count(text[i])
    dict[key]=val
    
print(dict)