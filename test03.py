test = 'hello_world_yoyo'
test2 = (test.split("_"))
print(test.split("_"))
print(test2)

k=0
for i in range (1,10):
    for j in range (1,i+1):
        k = i * j
        print ("%d x %d = %2d "%(i,j,k),end = " ")
    print ( )
