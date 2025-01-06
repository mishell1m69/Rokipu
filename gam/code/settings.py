f = open("./resources/settings.txt", "r")

key=["UP","LEFT","DOWN","RIGHT"]
values=[]
for line in f:
  values.append(int(line))
f.close()
KEYS={}
for k in range(len(key)):
  KEYS[key[k]]=values[k]

f = open("./resources/palette.txt", "r")
PALETTE=[[255,0,0]]
"""
for line in f:
  PALETTE.append(line)
"""
f.close()