'''Remove all versions in requirements.txt'''

with open('requirements.txt', 'r') as file:
    lines = file.readlines()
    

lines = [line.split('==')[0] + '\n' for line in lines]
# print(f"Lines after split: {lines}")
with open('requirements.txt', 'w') as file:
    file.writelines(lines)