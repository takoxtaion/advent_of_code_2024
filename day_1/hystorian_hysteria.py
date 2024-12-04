#part one
with open('day_1/input.txt', 'r') as file:
    content = file.read()
id = content.split()

my_list = list(map(int, id))

left_side = sorted(my_list[0::2])
right_side = sorted(my_list[1::2])

distance = 0

for i in range(0, len(left_side)):
    list = []
    list.append(left_side[i])
    list.append(right_side[i])
    distance += max(list) - min(list)

print(distance)

#part two
# with open('day_1/input.txt', 'r') as file:
#     content = file.read()
# id = content.split()

# my_list = list(map(int, id))

# left_side = my_list[0::2]
# right_side = my_list[1::2]

# similarity = 0
# for left_num in left_side:
#     similarity += left_num * right_side.count(left_num)
    
# print(similarity)