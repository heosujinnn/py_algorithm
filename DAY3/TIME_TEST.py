import time 
import random 

start_time=time.time()
array=[]
for v in range(2000):
    array.append(random.randint(0,10))
for i in array:
    for j in array:
        temp=i*j 
        #print(temp)
print(temp)
end_time=time.time()
print("time:",end_time-start_time)