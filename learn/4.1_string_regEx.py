import re

s1="Iron Maiden is the best album"

pattern=r"Iron Maiden"
print("1.) ", end="")
result=re.search(pattern,s1)

print(result)

if result:
  print("Match found.")
else:
  print("Match not found.")

