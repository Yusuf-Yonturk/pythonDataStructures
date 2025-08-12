# L=["Iron Maiden","Heavy Metal","Fear of the Dark",1992]
# print(["Iron Maiden","Heavy Metal","Fear of the Dark",1992])
# print(L)
# print(L[2:4])

# L.extend(["Favorite",9])
# print(L)

# L.append(["Favorite",9])
# print(L)

# L[5]=10
# print(L)

# del(L[6])
# print(L)

# list_split="A B C D".split()
# print(list_split)

# list_comma="A,B asd,C,D".split(",")
# print(list_comma)

# # B=L
# # print(B)

# # B[1]=L[0]
# # print(B)
# #####################################
# A=[1,'a']
# B=[2,1,'d']
# print(A+B)

# # Shopping List #
# Shopping_list=[]
# print(Shopping_list)
# #Extend the list
# Shopping_list.extend(['Laptop','Shoes','Tablet','Pen',"Watch",'Clothes'])
# print(Shopping_list)
# #Append
# Shopping_list.append("Basketball")
# print(Shopping_list)
# #Print last item
# print(Shopping_list[-1])
# #Print Watch and Clothes
# print(Shopping_list[-3:-1])
# #Replace "Pen" with "Notebook"
# Shopping_list[3]="Notebook"
# print(Shopping_list)
# #Del Clothes
# del(Shopping_list[5])
# print(Shopping_list)

#################################################
#################### Tuples #####################
#################################################

tuple1=("Hey",'Merhaba',2024,1.5)
print(tuple1)

print(type(tuple1))


print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])

print(tuple1[-1])
print(tuple1[-2])

tuple2=('Heavy Metal',10)+tuple1
print(tuple2)

print(tuple2[0:3])
print(tuple2[3:5])
print(len(tuple2))

Ratings=(3,4,5,1,2,6,7,9,8,10)
RatingsSorted=sorted(Ratings)
print(Ratings)
print(RatingsSorted)#Listeye çevirdi

Nested_tuple=(3,4,("RBAC","LLM",'multi-tenant','slo or p95'),(4,5),("RAG",(5,4)))
print(Nested_tuple)
print("Element 0 ", Nested_tuple[0])
print("Element 1 ", Nested_tuple[1])
print("Element 2 ", Nested_tuple[2])
print("Element 3 ", Nested_tuple[3])
print("Element 4 ", Nested_tuple[4])

print("Element 2, 0 ",   Nested_tuple[2][0])
print("Element 2, 1 ",   Nested_tuple[2][1])
print("Element 3, 0 ",   Nested_tuple[3][0])
print("Element 3, 1 ",   Nested_tuple[3][1])
print("Element 4, 0 ",   Nested_tuple[4][0])
print("Element 4, 1 ",   Nested_tuple[4][1])

print(Nested_tuple[2][1][0])
print(Nested_tuple[2][1][1])
print(Nested_tuple[2][1][2])


genres_tuple = ("RBAC", "multi-tenant", "soul", "heavy metal", "AI", \
"R&B", "RAG", "LLM")
print(genres_tuple)

## Cheat Sheet
my_list = [10, 2, 3, 4, 5] 
new_list = my_list.copy()
print(new_list) 
# Output: [10, 2, 3, 4, 5]

my_list = [3, 2, 2, 3, 4, 2, 5, 2] 
count = my_list.count(2)
print(count) 
# Output: 4

my_list = [1, 2, 3, 4, 7] 
my_list.insert(2, 6) 
print(my_list)
# Output: [1, 2, 6, 3, 4, 7]

my_list = [10, 25, 30, 40, 50] 
removed_element = my_list.pop() # Removes and returns the last element 
print(removed_element) 
# Output: 50 

print(my_list) 
# Output: [10, 25, 30, 40]

my_list = [10, 25, 30, 40, 50] 
my_list.remove(30) # Removes the element 30 
print(my_list) 
# Output: [10, 25, 40, 50]

my_list = [1, 2, 3, 4, 7] 
my_list.reverse()
print(my_list) 
# Output: [7, 4, 3, 2, 1]

my_list = [0, 2, 3, 4, 5] 
print(my_list[1:4]) 
# Output: [2, 3, 4] (elements from index 1 to 3)

print(my_list[:3]) 
# Output: [0, 2, 3] (elements from the beginning up to index 2) 

print(my_list[2:]) 
# Output: [3, 4, 5] (elements from index 2 to the end) 

print(my_list[::2]) 
# Output: [0, 3, 5] (every second element)

my_list = [4, 2, 8, 1, 9] 
my_list.sort() 
print(my_list) 
# Output: [1, 2, 4, 8, 9] 

my_list = [5, 2, 7, 1, 9] 
my_list.sort(reverse=True) 
print(my_list) 
# Output: [9, 7, 5, 2, 1]

fruits = ("apple", "banana", "apple", "cherry")
print(fruits.count("apple")) #Counts the number of times apple is found in tuple.
#Output: 2

numbers = (10, 40, 5, 30)
print(sum(numbers))
#Output: 85

numbers = (10, 20, 4, 40)
print(min(numbers))  
#Output: 4
print(max(numbers))
#Output: 40

fruits = ("apple", "banana", "cherry")
print(len(fruits)) #Returns length of the tuple.
#Output: 3