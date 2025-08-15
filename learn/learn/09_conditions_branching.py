age=19
if(age>18):
  print("you can enter")

elif(age==18):
  print("go see Iron Maiden")
else:
  print("you can't enter")
print("move on")

result=True
print(result)
print(not(result))

a=True
b=True
print(a or b)
print(a or not(b))
print(not(a) or b)
print(not(a) or not(b))

album_year=1992
#for 1970 - 1999
if (album_year < 1980) or (album_year > 1990):
  print("This Album was made in the 70's or 90")
else:
  print("The Album was made in the 1980's")

if(album_year >1979) and (album_year <1990):
  print("The Album was made in the 1980's")


player="Serena Williams"
sport="Tennis"
achievements=23

if(sport=='Tennis') or (achievements==20):
    print(f"{player} plays {sport} or has {achievements} achievements")
else:
    print(f"{player} doesn't not meet the criteria.")

player="Usain Bolt"
sport="Athletics"
achievements= 8

if(achievements < 10) and (sport!="Soccer"):
    print(f"{player} plays {sport} and has only {achievements} achievements.")
else:
    print(f"{player} doesn't meet the criteria.")
