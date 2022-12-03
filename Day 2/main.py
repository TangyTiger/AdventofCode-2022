total = 0

with open("input.txt", 'r') as data_file:
    for line in data_file:
        data = line.split()
        print(data)
        if data[0] == "A":
            if data[1] == "X":
                total+=3
            elif data[1] == "Y":
                total+=4
            else:
                total+=8
        elif data[0] == "B":
            if data[1] == "X":
                total+=1
            elif data[1] == "Y":
                total+=5
            else:
                total+=9
        else:
            if data[1] == "X":
                total+=2
            elif data[1] == "Y":
                total+=6
            else:
                total+=7
        
print(total)