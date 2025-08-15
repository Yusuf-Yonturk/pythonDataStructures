print(range(5,10))

renkler =["red", 'yellow', "blue"]
for renk in renkler:
  print(renk)   

renkler = ["red","yellow",'blue']
for renk in enumerate(renkler):
    print(renk)

squares=["white","white","white","black","red","blue"]
new_squares=[]

i=0 

while(squares[i]=="white"):
   new_squares.append(squares[i])
   i=i+1

print(new_squares)

dates=[1992,2003,1980]

N=len(dates)

for i in range(N):
   print(dates[i])

for i in range(10):
   print(i)

for year in dates:
   print(year)

squar=["red","white",'green',"black","blue"]
for i in range(0,5):
   print("Before square",i,'is',squar[i])
   squar[i]='white'
   print("After square",i,"is",squar[i])
print(squar)

squaresa=['red', 'yellow', 'green', 'purple', 'blue']

for i, squarez in enumerate(squaresa):
    print(i, squarez)

datess=[1982, 1980, 1973, 2000]

i=0
year=datess[0]

while(year !=1973):
   print(year)
   i=i+1
   year=datess[i]

print("It took",i,"repetitions to get out of loop.")

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
while(PlayListRatings[i]>6 and len(PlayListRatings)):
    print(PlayListRatings[i])
    i=i+1

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []

for color in squares:
    if color=="orange":
        new_squares.append(color)
    else:
        break
print(new_squares)

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(i < len(squares) and squares[i] == 'orange'):
    new_squares.append(squares[i])
    i = i + 1
print (new_squares)