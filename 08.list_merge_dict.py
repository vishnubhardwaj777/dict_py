from dataclasses import dataclass


num1=eval(input("How many element enter in List 1 : "))
l1=[]
for e in range(num1):
    l1.append(eval(input("Enter Item : ")))

print('\n')    
print(l1)

num2=eval(input("How many element enter in List 2 : "))
l2=[]
for e in range(num2):
    l2.append(eval(input("Enter Item : ")))

print('\n')    
print(l2)

d1={}

for key in l1:
    for value in l2:
        d1[key]=value
        l2.remove(value)
        break

print(d1)
