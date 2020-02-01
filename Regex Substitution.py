import re
dict = {" && ":" AND ",
        " || ":" OR "}

para=[]
l = int(input())
for i in range(l):
    para.append(input())

for line in para:
    line = str(re.sub(r" &&(?= )"," and",line))
    line = re.sub(' \|\|(?= )',' or',line)
    print(line)
