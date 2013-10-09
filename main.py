# -*- coding: cp936 -*-
import random
from time import time
from closest import closestpair,sqdist
from closest2 import closestpair2


def timeTest1(points):
    print "BigTheta(nlgn) method:"
    start = time()
    print("Start: " + str(start))
    ans1 = closestpair(points)
    stop = time()
    print("Stop: " + str(stop))
    print(str(stop-start) + "秒")
    print "closest points pair:"
    print ans1
    print "closest distance:" + str(sqdist(ans1[0],ans1[1]))

def timeTest2(points):
    print "BigTheta(n^2) method:"
    start = time()
    print("Start: " + str(start))
    ans2 = closestpair2(points)
    stop = time()
    print("Stop: " + str(stop))
    print(str(stop-start) + "秒")
    print "closest points pair:"
    print ans2
    print "closest distance:" + str(sqdist(ans2[0],ans2[1]))
    
def main():
    n = input("input the number of points:")
    points = []
    for i in range(n):
        x = random.uniform(0, n)
        y = random.uniform(0, n)
        points.append([x,y])
    timeTest1(points)
    timeTest2(points)
    n = input("Input any key to exit:")
if __name__=='__main__':
    main()
