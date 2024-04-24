import time

start = time.time()
i=1
while i<2:
    print(i)
    i+=1
print(time.time()-start)

x = [1,2,3,4,5,6]
sum = 0
# For first loop
for i in x:
    sum = sum+i
print(sum)
print(time.time()-start)

# For Second loop
product = 1
for i in x:
    product = product*i
print(product)
print(time.time()-start)