count = 0


with open("Day 4\input.txt", 'r') as data_file:
    for line in data_file:
        data = line.split(",")
        data[1] = data[1].strip()
        data[0] = data[0].split("-")
        data[1] = data[1].split("-")
        print(data)
        if int(data[0][0]) <= int(data[1][0]) and int(data[0][1]) >= int(data[1][1]):
            count+=1
        elif int(data[1][0]) <= int(data[0][0]) and int(data[1][1]) >= int(data [0][1]):
            count+=1

print(count)