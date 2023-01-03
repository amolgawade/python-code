'#factorial program bye def'

x = int(input("Enter the factorial number"))
res = 1
for i in range(1, x+1):
    res = res * i
print(res)

# initialize x = 1
# iterate i from 1 to n
# multiply i value with x and assign calculated result to x value
# print x