'''
Interclasare elemente liste, cu elemente
ordonate crescator.

ex:
l1 = [1, 3, 3, 12]
l2 = [2, 6, 9]


li = [1, 2, 3, 3, 6, 9, 12]
'''

l1 = [1, 3, 3, 12, 18]
l2 = [0, 2, 15]
li = []

print("l1:", l1)
print("l2:", l2)

n = len(l1)
m = len(l2)
print("n:", n, "m:", m)

i = 0
j = 0

# parcurgere in paralel liste
while(i < n and j < m):
    if l1[i] <= l2[j]:
        li.append(l1[i])
        i += 1
    else:
        li.append(l2[j])
        j += 1

print("i:", i, "j:", j)
        
print(li)


# doar una din bucle se va executa
# pentru vectorul cu lungime mai mare ca 
while(i < n):
    li.append(l1[i])
    i += 1

while(j < m):
    li.append(l2[j])
    j += 1

print(li)
