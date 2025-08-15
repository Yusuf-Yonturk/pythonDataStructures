#Create the dictionary
Dict= {"key1":"Hi","key2":"2","key3": [3,3,3], "key4":(4,4,4), ('key5'):5, (0,6):1}
print(Dict)

print(Dict["key1"])
print(Dict[(0,6)])

iron_maiden_albums = {
    "Iron Maiden": "1980",
    "Killers": "1981",
    "The Number of the Beast": "1982",
    "Piece of Mind": "1983",
    "Powerslave": "1984",
    "Somewhere in Time": "1986",
    "Seventh Son of a Seventh Son": "1988",
    "No Prayer for the Dying": "1990",
    "Fear of the Dark": "1992",
    "The X Factor": "1995",
    "Virtual XI": "1998",
    "Brave New World": "2000",
    "Dance of Death": "2003",
    "A Matter of Life and Death": "2006",
    "The Final Frontier": "2010",
    "The Book of Souls": "2015",
}
print(iron_maiden_albums)

print(iron_maiden_albums['Fear of the Dark'])

print(iron_maiden_albums.keys())
print(iron_maiden_albums.values())

iron_maiden_albums['Senjutsu']='2021'
print(iron_maiden_albums)

del(iron_maiden_albums['Virtual XI'])
print(iron_maiden_albums)
print('Virtual XI' in iron_maiden_albums)

iron_maiden_albums['Virtual XI']='1998'
print(iron_maiden_albums)
print('Virtual XI' in iron_maiden_albums)

############## Create an empty dictionary
inventory={}
############## First product details in variable
product1_name="Mobil Phone"
product1_quantity=5
product1_price=20000
product1_release_year=2025
############## Add the details in inventory
inventory['Product1 Name']=product1_name
inventory['Product1 Quantity']=product1_quantity
inventory['Product1 Price']=product1_price
inventory["Product1 Release Year"]=product1_release_year
print(inventory)
print("///////////////////////////")

product2_name = "Laptop"
product2_quantity = 10
product2_price = 50000
product2_release_year= 2023

inventory['Product2 Name']=product2_name
inventory['Product2 Quantity']=product2_quantity
inventory['Product2 Price']=product2_price
inventory["Product2 Release Year"]=product2_release_year
print(inventory)
################# Check if
print("Product2 Release Year" in inventory)
################# Del
del(inventory["Product1 Release Year"])
del(inventory["Product2 Release Year"])
print(inventory)
print(list(inventory.keys()))

