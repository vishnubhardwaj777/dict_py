from heapq import merge


num1=eval(input("How many enter element in dict 1 : "))
dict1={}
for i in range(num1):
    key=eval(input("Enter Key : "))
    data=eval(input("Ebter data : "))
    dict1[key]=data

print(dict1)

num2=eval(input("How many enter element in dict 2 : "))
dict2={}
for i in range(num2):
    key=eval(input("Enter Key : "))
    data=eval(input("Ebter data : "))
    dict2[key]=data

print(dict2)

d3={}
d3=merge(dict1,dict2)
print(d3)

# Not Complete Yet.............OK