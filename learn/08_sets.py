print(set((11,22,"sad","sad",3)))

A={"Data","Structures","Software","Engineering"}

A.add("Python")
print(A)

A.add("Python")
print(A)

A.add("C++")
print("C++" in A)
print(A)

A.remove("C++")
print("C++" in A)
print(A)

###### Intersect
B={"Java","C","C++","C#","Paper","Software","skydiving","scubadiving","Engineering"}
C=A & B
print(C)
###### Difference
print(B.difference(A))
###### Intersect
print(A.intersection(B))
###### Union
D=A.union(B)
print(D)
###### Subset Superset
A={"apple", "pear"}
B= {"apple", "pear", "banana"}
print(A.issubset(B))
print(B.issubset(A))
print(B.issuperset(A))
print(A.issuperset(B))
B=list(B)
print(B)