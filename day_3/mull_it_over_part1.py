#part 1
import re

with open('day_3/input.txt', 'r') as file:
    content = file.read()

pattern = "mul\(\d+,\d+\)"

matches = re.findall(pattern, content)

total = 0

for match in matches:
    num_list = match[match.find("(") + 1:match.find(")")].split(",")
    total +=  int(num_list[0]) * int(num_list[1])
print(total)
        


