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

	def actionSet(self):
		################# [ h,  w, cost]
		self.actionset = [[ 1,  0, 1],
						  [ 0,  1, 1],
						  [-1,  0, 1],
						  [ 0, -1, 1],
						  [ 1,  1, np.sqrt(2)],
						  [ 1, -1, np.sqrt(2)],
						  [-1,  1, np.sqrt(2)],
						  [-1, -1, np.sqrt(2)]]
		pass

	def checkEnd(self, currentNode):
		return self.end == currentNode

	def findNewPose(self, nodeState, action):
		tmp = nodeState[2]
		tmp = (tmp[0]+action[0], tmp[1]+action[1])
		return tmp

	def dijNewPose(self, node, action):
		tmp = (node[0]+action[0], node[1]+action[1])
		return tmp

	def viewer(self, num):
		self.showCounter += 1
		if self.showCounter%num == 0:
			cv2.imshow("Solver", self.obss.animationImage)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				self.view = False
		pass

	def trackBack(self):
		path = [self.end]
		tmp = self.end
		while tmp!=self.start:
			self.obss.path(tmp)
			temp = self.obss.getParent(tmp)
			tmp = (int(temp[0]), int(temp[1]))
			# print(tmp)
			path.append(tmp)
			self.viewer(1)
		return

	def DijkstarSolve(self):
		heappush(self.Data, (0, self.start))
		while len(self.Data) > 0:
			cost, node = heappop(self.Data)
			if self.checkEnd(node):
				self.goalReach = True
				print("goal reached")
				self.trackBack()
				return
			for action in self.actionset:
				newPose = self.dijNewPose(node, action)
				if self.obss.checkFeasibility(newPose):
					newCost = cost + action[2]
					if self.obss.checkVisited(newPose):
						self.obss.addExplored(newPose)
						self.obss.addParent(newPose, node, newCost)
						heappush(self.Data, (newCost, newPose))
					else:
						if self.obss.getCost(newPose) > newCost:
							# self.obss.addExplored(newPose)
							self.obss.addParent(newPose, node, newCost)
					if self.view:
						self.viewer(30)
		print("Could not find goal node...Leaving..!!")
		return 


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

solver = PathFinder(start, end, r, c)
solver.view = int(Args.ShowAnimation)
solver.skipFrame = int(Args.Framerate)

if solver.initialCheck():
	startTime = time.time()
	solver.DijkstarSolve()
	print(time.time() - startTime)
	print("Press (q) to exit")
	solver.viewer(1)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
else:
	pass