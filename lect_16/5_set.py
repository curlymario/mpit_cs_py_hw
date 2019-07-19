A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
# for x in A:
#     if x not in B:
#         print(x)

print({x for x in A if x not in B})

# ==================================

A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')

E = A.difference(B).intersection(C.difference(D)).union(D.difference(A).intersection(B.difference(C)))
print(E)

F = A.difference(B)
G = C.difference(D)
H = D.difference(A)
I = B.difference(C)
J = F.intersection(G)
K = H.intersection(I)
E = J.union(K)
print(E)