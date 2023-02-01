num=int(input("How many element enter in dict : "))
d1={}
for e in range(num):
    key=eval(input("Enter Key : "))
    data=eval(input("Enter Data : "))
    d1[key]=data
print('\n')
for i,k in d1.items():
    print(i,k)    
print('\n')    