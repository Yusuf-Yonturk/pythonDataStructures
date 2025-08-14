album_ratings=[10.0, 8.5, 9.5, 7.0, 8.0, 9.5, 9.0, 9.5]
print(album_ratings)
print(sorted(album_ratings))
print(album_ratings)
album_ratings.sort()
print(album_ratings)

#######################

isimler = ["Ali", "Ayse", "Mehmet"]

def selamla(liste):
    print(liste)

selamla(isimler)

#######################

isimler = ["Ali", "Ayse", "Mehmet"]

def selamla(*args):
    print(args)

selamla(*isimler)

#######################

def add_c(x):
    print("Fonksiyon basinda ID:", id(x))
    x = x + "DC"
    print("Fonksiyon sonunda ID:", id(x))
    print("Fonksiyon icindeki x:", x)
    return x

#######################

x = "AC"
print("Fonksiyon cagrilmadan once ID:", id(x))
z = add_c(x)
print("Fonksiyon cagrildiktan sonra disaridaki x:", x)
print("z degiskeni:", z)

#######################

def fear_of_the_dark():
    Date=1992
    return(Date)
Date=2025
print(fear_of_the_dark())

#######################

def ironmaiden(y):
    print(Rating)
    return Rating+y

Rating = 9

Z = ironmaiden(1)
print(Rating)
print(Z)

#######################

def PinkFloyd():
    global ClaimedSales
    ClaimedSales="45 million"
    return ClaimedSales

PinkFloyd()
print(ClaimedSales)

#######################

x = "AC"
def add_dc(x):
    x = x + "DC"
    return x

y = add_dc(x)
print(x)   # AC
print(y)   # ACDC

#######################

x = "AC"
def add_dc():
    global x
    x = x + "DC"

add_dc()
print(x)   # ACDC

#######################

def greet(name):
    return "Hello, " + name
result = greet("Yusuf")
print(result)  # Output: Hello, Yusuf


global_variable = "I'm global"
def example_function():
    local_variable = "I'm local"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable

example_function()

global_variable = "I'm global"

def example_function():
    global_variable = "Changed"  # Bu yeni bir local değişken oluşturur
    print(global_variable)

example_function()
print(global_variable)


global_variable = "I'm global"

def example_function():
    global global_variable
    global_variable = "Changed"  # Artık global olanı değiştirir

example_function()
print(global_variable)  # "Changed"


my_list=[]

def add_element(data_structure, element):
    data_structure.append(element)

def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} wasn't found in {data_structure} ")

add_element(my_list,"elma")
print(my_list)
remove_element(my_list, 'elmas')
print(my_list)



def findw(sentence):
    count=0
    for w in sentence.lower().split():
        
        if w == word :
            count+=1
    print(count)            
word="little"
sentence="Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that"\
"Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"
findw(sentence)
