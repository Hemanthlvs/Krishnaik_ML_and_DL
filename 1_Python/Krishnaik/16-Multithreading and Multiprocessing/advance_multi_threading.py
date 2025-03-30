### Multithreading With Thread Pool Executor
#for example if you have a multiple tables and you want to loop them in for loop 
# and access it and do some on it. for that you need to connect to server multiple times 
# and that is nothing but an i/o operation. so for multiple I/O operations its better to use multithreading.

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1) #consider this as a I/O operation.
    return f"Number :{number}"

numbers=[1,2,3,4,5,6,7,8,9,0,1,2,3] #consider these as tables

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_number,numbers)

for result in results:
    print(result)