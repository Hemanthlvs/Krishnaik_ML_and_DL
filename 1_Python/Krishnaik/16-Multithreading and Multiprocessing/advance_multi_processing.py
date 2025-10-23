###  Multiprocessing with ProcessPoolExecutor
#since we are using spark we dont need to use this multi processing.
#this is used when you are dealing with large computation operations which depends on cpu bound. 
# for us, spark will do this as a default.

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square: {number * number}"

numbers=[1,2,3,4,5,6,7,8,9,11,2,3,12,14]
if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_number,numbers)

    for result in results:
        print(result)