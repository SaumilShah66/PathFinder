import sys
sys.path.remove(sys.path[1])
import cv2
import numpy as np
from obstacle import Obstructions
import time
import argparse
from heapq import heappush, heappop








Parser = argparse.ArgumentParser()
Parser.add_argument('--Start', default="[5,5]", help='Give inital point')
Parser.add_argument('--End', default="[290,190]", help='Give inital point')
Parser.add_argument('--RobotRadius', default=2, help='Give inital point')
Parser.add_argument('--Clearance', default=2, help='Give inital point')
Parser.add_argument('--ShowAnimation', default=1, help='1 if want to show animation else 0')
Parser.add_argument('--Framerate', default=30, help='Will show next step after this many steps. Made for fast viewing')
Args = Parser.parse_args()

start = Args.Start
end = Args.End
r = int(Args.RobotRadius)
c = int(Args.Clearance)

start = [int(i) for i in start[1:-1].split(',')]
start[1] = 200 - start[1]
end = [int(i) for i in end[1:-1].split(',')] 
end[1] = 200 - end[1]