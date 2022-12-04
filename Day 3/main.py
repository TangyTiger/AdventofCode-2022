total=0
results = []
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def split_list(lst):
    
    middle = int(len(lst[0])/2)
    return [lst[0][:middle], lst[0][middle:]]

with open("Day 3\input.txt", 'r') as data_file:
    for line in data_file:
        data = line.split()
        split = split_list(data)
        brk = False
        for i in split[0]:
            if brk:
                break
            for j in split[1]:
                if i==j:
                    results.append(i)
                    brk = True
                    break

for i in results:
    
    if i.isupper():
        total+=26
    i = i.lower()
    total+=letters.index(i)+1
print(total)
