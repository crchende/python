'''
Vector de lungime n, cu elem. numerice
Un nr k, 0 < k < n-1
Gasiti secventa din vector de lungime k
de suma maxima.
'''

lst = [10, 10, 5, -2, 6, -1, 20]
k = 4
x = k
#print(lst[1:3])
print("lst:        ", lst)
print("k:", k)

lst_sm_part = [lst[0]]

for i in range(1, len(lst)):    
    lst_sm_part.append(lst_sm_part[i-1] + lst[i])
    

print("lst_sm_part:", lst_sm_part)
#       7, 8, 13, 11, 17, 16

# sume de lungime k, de la i, la i+k-1
# s_k = s[i+k-1] - s[i]

tpl_index_max = (0, k-1)
max = lst_sm_part[k-1]
for i in range(k, len(lst)):
    sm2 = lst_sm_part[i] - lst_sm_part[i-k]
    print("sm2 =", sm2)
    if max < sm2:
        max = sm2
        tpl_index_max = (i-k+1, i)
        
print("max =    ", max)
print("indecsi: ", tpl_index_max)
print("elemente:", lst[tpl_index_max[0]:tpl_index_max[1]+1])
