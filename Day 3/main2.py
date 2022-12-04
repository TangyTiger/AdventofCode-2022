count = 0
num = 0
total=0
temp = []
groups = []
results = []
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


with open("Day 3\input.txt", 'r') as data_file:
    for line in data_file:
        count+=1
        temp.append(line.split())
        if count%3 == 0:
            groups.append(temp)
            temp = []

for i in range(len(groups)):
        for k in range(len(groups[i][0][0])):
            try: 
                groups[i][1][0].index(groups[i][0][0][k])
                groups[i][2][0].index(groups[i][0][0][k])
                results.append(groups[i][0][0][k])
                break
                
            except ValueError:
                continue
           
                

print(len(results))

for i in results:
    
    if i.isupper():
        total+=26
    i = i.lower()
    total+=letters.index(i)+1
print(total)


# for i in results:
#     if i.isupper():
#         total+=26
#     i = i.lower()
#     total+=letters.index(i)+1
# print(total)
