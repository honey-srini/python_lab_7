import functools
 

list = []
for i in range(1,11):
    list.append(i)

print(list)

print("The sum of the first 10 natural numbers : ", end="")
print(functools.reduce(lambda a, b: a+b, list))
 
