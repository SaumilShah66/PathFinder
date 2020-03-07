import sys
sys.path.remove(sys.path[1])
import cv2
import numpy as np
from obstacle import Obstructions
import time
import argparse
from heapq import heappush, heappop


class PathFinder():
	def __init__(self, start, end, robotRadius, clearance):
		self.start = (start[1], start[0])
		self.end = (end[1], end[0])
		self.allNodes = []
		############### nodeID [0], pareent [1], node [2], cost [3]  ## For BFS
		# self.mainData = [[0, 0, self.start, 0]]
		############### cost , node  #### For Dijkstar
		self.Data = []
		self.allPose = [self.start]
		self.actionSet()
		self.possibleMove = len(self.actionset)
		self.temp = []
		self.obss = Obstructions(300,200, robotRadius, clearance)
		self.goalReach = False
		self.view = True
		self.finalGoalState = []
		self.trace = []
		self.showCounter = 0
		self.skipFrame = 1

	def initialCheck(self):
		if not self.obss.checkFeasibility(self.start):
			print("Start node is in obstacle field. Please provide correct starting position.")
			return False
		elif not self.obss.checkFeasibility(self.end):
			print("Goal node is in obstacle field. Please provide correct goal position.")
			return False
		else:
			return True





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