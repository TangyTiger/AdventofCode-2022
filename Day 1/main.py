max = 0
temp = 0
myList = []


with open("input.txt", 'r') as data_file:
    for line in data_file:
        data = line.split()
        #print(data)
        if len(data) == 1:
            temp+=int(data[0])
        elif len(data) == 0:

            myList.append(temp)
                
            temp=0
myList.sort()
print(myList[-1]+myList[-2]+myList[-3])
        
        


# fileObject = open("input.txt", "r")
# data = fileObject.read()
# print("hello world")
# max = 0
# max2 = 0
# number = ""
# # print(data[0])

# for i in range(len(data)-1):






#     if data[i] == "\n":
#         if data[i+1] == "\n":
#             if max2>max:
#                 max = max2
#         else:
#             for j in range(20):
                
#                 if data[i+j] != "\n":
#                     print("hi")
#                     number+=data[i+j]
#                 else:
#                     break
            

  
        


# for i in range(len(data)-1):

#     if data[i] != " " and data[i] != "\n":
#         for j in range(len(data)-1):
#             if data[i+j] != " " and data[i+j] != "\n":
#                 max2+=int(data[i+j])
#             else:
#                 if data[i+j+1] == " " or data[i+j+1] == "\n":
#                     break
#     #print(f"max 2: {max2}")
#     if data[i] == "\n" and data[i+1] == "\n":
#            if max2 > max:
#                 max = max2
#                 #print(max)

# print(max)