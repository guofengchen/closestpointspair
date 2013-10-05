# -*- coding: cp936 -*-
import random
#random.uniform(0, 1000000)
from time import time

def timeTest():
    start = time()
    print("Start: " + str(start))
    for i in range(1, 1000000):
        random.uniform(0, 1000000)
    stop = time()
    print("Stop: " + str(stop))
    print(str(stop-start) + "秒")
    
def main():
    timeTest()

if __name__=='__main__':
    main()
