name="Yusuf"
age=20
sentence=f"My name is {name} and I am {age} years old."
print(sentence)

name="Jonathan"
age=25
sentenceF="My name is {} and I am {} years old.".format(name, age)
print(sentenceF)

name="Merlin"
age=60
sentenceP="My name is %s and I am %d years old." % (name,age)
print(sentenceP)

x=10
y=5
print(f"The sum of x and y is {x+y}.")

regular_string="C:\new_folder\file.txt"
print("Regular String:", regular_string)

raw_string=r"C:new_folder\file.txt"
print("Raw String:", raw_string)