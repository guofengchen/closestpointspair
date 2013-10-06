# -*- coding: cp936 -*-
import random
from time import time
from closest import closestpair
from closest2 import closestpair2


def timeTest1(points):
    start = time()
    print("Start: " + str(start))
    ans1 = closestpair(points)
    stop = time()
    print("Stop: " + str(stop))
    print(str(stop-start) + "秒")
    print ans1

def timeTest2(points):
    start = time()
    print("Start: " + str(start))
    ans2 = closestpair2(points)
    stop = time()
    print("Stop: " + str(stop))
    print(str(stop-start) + "秒")
    print ans2

    
def main():
    points = []
    for i in range(1000000):
        x = random.uniform(0, 1000000)
        y = random.uniform(0, 1000000)
        points.append([x,y])
    timeTest1(points)
    timeTest2(points)
if __name__=='__main__':
    main()
