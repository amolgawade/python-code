filename = "siddhartha.txt"
with open(filename) as f_obj:
    content = f_obj.read()

print(content)


filename = "siddhartha.txt"
with open(filename) as f_obj:
    for line in filename:
        print(line)

filename = "siddhartha.txt"
with open(filename) as f_obj:
    lines = f_obj.readlines()
for line in lines :
    print(line.rstrip())
