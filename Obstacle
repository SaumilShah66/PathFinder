import matplotlib.pyplot as plt
import numpy as np
import math


class Obstructions():
    def __init__(self, width, height, r, c):
        self.W = width +1
        self.H = height +1
        self.r = r
        self.c = c
        self.showObstacle = False
        self.map = np.zeros([self.H, self.W], dtype=np.int8)
        self.animationImage = np.zeros([self.H, self.W, 3])
        self.generateMap()
        #self.showMap()
        self.r = 0
        self.c = 0
        self.showObstacle = True
        self.generateMap()
        self.explored = self.map.copy()
        self.parentData = np.zeros([self.H, self.W, 3])
        pass

    def generateMap(self):
        self.circle((225, 50), 25)
        self.ellipse((150, 100), 20, 40)
        self.quad1((25, 15), (75, 15), (50, 50), (20, 80), (100, 50))
        self.quad2((75, 15), (100, 50), (75, 80), (50, 50), (25, 15))
        self.quad3((225, 160), (250, 175), (225, 190), (200, 175))
        self.quad4((35, 123), (100, 161), (95, 170), (30, 132))
        self.border()
        pass

    def circle(self, center, radius):
        center_x, center_y = center[0], center[1]
        for i in range(center_x - (radius + self.r + self.c), center_x + (radius + self.r + self.c)):
            for j in range(center_y - (radius + self.r + self.c), center_y + (radius + self.r + self.c)):
                if ((i - center_x) ** 2 + (j - center_y) ** 2) <= (radius + self.r + self.c) ** 2:
                    if not self.showObstacle:
                        self.map[j, i] = 1
                    else:
                        self.animationImage[j,i] = np.array([255,255,255])
        return

    def ellipse(self, center, semiminor, semimajor):
        center_x, center_y = center[0], center[1]
        for i in range(center_x - (semimajor + self.r + self.c), center_x + (semimajor + self.r + self.c)):
            for j in range(center_y - (semiminor + self.r + self.c), center_y + (semiminor + self.r + self.c)):
                if (((i - center_x) / (semimajor + self.r + self.c)) ** 2 + ((j - center_y) / (semiminor + self.r + self.c)) ** 2) <= 1:
                    if not self.showObstacle:
                        self.map[j, i] = 1
                    else:
                        self.animationImage[j,i] = np.array([255,255,255])
        return


    def quad1(self, vertex1, vertex2, vertex3, vertex4, vertex5):
        x1, y1 = vertex1[0], vertex1[1]
        x2, y2 = vertex2[0], vertex2[1]
        x3, y3 = vertex3[0], vertex3[1]
        x4, y4 = vertex4[0], vertex4[1]
        x5, y5 = vertex5[0], vertex5[1]
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y3 - y2) / (x3 - x2)
        m3 = (y4 - y3) / (x4 - x3)
        m4 = (y1 - y4) / (x1 - x4)
        m5 = (y5 - y2) / (x5 - x2)
        x = [x1, x2, x3, x4, x5]
        y = [y1, y2, y3, y4, y5]
        for i in range(min(x) - 3*self.r - 3*self.c, max(x) + 3*self.r + 3*self.c):
            for j in range(min(y) - 3*self.r - 3*self.c, max(y) + 4*self.r + 4*self.c):
                if (j >= m1 * i + y1 - m1 * x1 - ((self.r + self.c) * math.sqrt((m1 ** 2) + 1))) and (
                        j <= m2 * i + y2 - m2 * x2 + ((self.r + self.c) * math.sqrt((m2 ** 2) + 1))) and (
                        j <= m3 * i + y3 - m3 * x3 + ((self.r + self.c) * math.sqrt((m3 ** 2) + 1))) and (
                        j >= m4 * i + y4 - m4 * x4 - ((self.r + self.c) * math.sqrt((m4 ** 2) + 1))):
                    if not self.showObstacle:
                        self.map[j, i] = 1
                    else:
                        self.animationImage[j,i] = np.array([255,255,255])
                if j <= m5 * i + y5 - m5 * x5 - ((self.r + self.c) * math.sqrt((m5 ** 2) + 1)):
                    if not self.showObstacle:
                        self.map[j, i] = 0
                    else:
                        self.animationImage[j,i] = np.array([0,0,0])
        return

    def quad2(self, vertex1, vertex2, vertex3, vertex4, vertex5):
        x1, y1 = vertex1[0], vertex1[1]
        x2, y2 = vertex2[0], vertex2[1]
        x3, y3 = vertex3[0], vertex3[1]
        x4, y4 = vertex4[0], vertex4[1]
        x5, y5 = vertex5[0], vertex5[1]
        x = [x1, x2, x3, x4, x5]
        y = [y1, y2, y3, y4, y5]
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y3 - y2) / (x3 - x2)
        m3 = (y4 - y3) / (x4 - x3)
        m4 = (y1 - y4) / (x1 - x4)
        m5 = (y5 - y1) / (x5 - x1)
        for i in range(min(x) - 3*self.r - 3*self.c, max(x) + 3*self.r + 3*self.c):
            for j in range(min(y) - 3*self.r - 3*self.c, max(y) + 3*self.r + 3*self.c):
                if (j >= m1 * i + y1 - m1 * x1 - ((self.r + self.c) * math.sqrt((m1 ** 2) + 1))) and (
                        j <= m2 * i + y2 - m2 * x2 + ((self.r + self.c) * math.sqrt((m2 ** 2) + 1))) and (
                        j <= m3 * i + y3 - m3 * x3 + ((self.r + self.c) * math.sqrt((m3 ** 2) + 1))) and (
                        j >= m4 * i + y4 - m4 * x4 - ((self.r + self.c) * math.sqrt((m4 ** 2) + 1))):
                    if not self.showObstacle:
                        self.map[j, i] = 1
                    else:
                        self.animationImage[j,i] = np.array([255,255,255])
                if j <= m5 * i + y1 - m5 * x1 - ((self.r + self.c) * math.sqrt((m5 ** 2) + 1)):
                    if not self.showObstacle:
                        self.map[j, i] = 0
                    else:
                        self.animationImage[j,i] = np.array([0,0,0])
        return

    def quad3(self, vertex1, vertex2, vertex3, vertex4):
        x1, y1 = vertex1[0], vertex1[1]
        x2, y2 = vertex2[0], vertex2[1]
        x3, y3 = vertex3[0], vertex3[1]
        x4, y4 = vertex4[0], vertex4[1]
        m1 = (y2 - y1)/(x2 - x1)
        m2 = (y3 - y2)/(x3 - x2)
        m3 = (y4 - y3)/(x4 - x3)
        m4 = (y1 - y4)/(x1 - x4)
        for i in range(0, 300):
            for j in range(0, 200):
                if (j >= m1*i + y1 - m1*x1 - ((self.r + self.c)*math.sqrt((m1**2)+1))) and (
                        j <= m2*i + y2 - m2*x2 + ((self.r + self.c)*math.sqrt((m2**2)+1))) and (
                        j <= m3*i + y3 - m3*x3 + ((self.r + self.c)*math.sqrt((m3**2)+1))) and (
                        j >= m4*i + y4 - m4*x4 - ((self.r + self.c)*math.sqrt((m4**2)+1))):
                    if not self.showObstacle:
                        self.map[j, i] = 1
                    else:
                        self.animationImage[j,i] = np.array([255,255,255])
        return

    def quad4(self, vertex1, vertex2, vertex3, vertex4):
        x1, y1 = vertex1[0], vertex1[1]
        x2, y2 = vertex2[0], vertex2[1]
        x3, y3 = vertex3[0], vertex3[1]
        x4, y4 = vertex4[0], vertex4[1]
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y3 - y2) / (x3 - x2)
        m3 = (y4 - y3) / (x4 - x3)
        m4 = (y1 - y4) / (x1 - x4)
        for i in range(0, 300):
            for j in range(0, 200):
                if (j >= m1 * i + y1 - m1 * x1 - ((self.r + self.c) * math.sqrt((m1 ** 2) + 1))) and (
                        j <= m2 * i + y2 - m2 * x2 + ((self.r + self.c) * math.sqrt((m2 ** 2) + 1))) and (
                        j <= m3 * i + y3 - m3 * x3 + ((self.r + self.c) * math.sqrt((m3 ** 2) + 1))) and (
                        j >= m4 * i + y4 - m4 * x4 - ((self.r + self.c) * math.sqrt((m4 ** 2) + 1))):
                    if not self.showObstacle:
                        self.map[j, i] = 1
                    else:
                        self.animationImage[j,i] = np.array([255,255,255])
        return

    def border(self):
        for i in range(0, 300):
            for j in range(0, 0 + self.r + self.c):
                if not self.showObstacle:
                    self.map[j, i] = 1
                else:
                    self.animationImage[j,i] = np.array([255,255,255])
        for i in range(0, 300):
            for j in range(200 - self.r - self.c, 200):
                if not self.showObstacle:
                    self.map[j, i] = 1
                else:
                    self.animationImage[j,i] = np.array([255,255,255])
        for i in range(0, 0 + self.r + self.c):
            for j in range(0, 200):
                if not self.showObstacle:
                    self.map[j, i] = 1
                else:
                    self.animationImage[j,i] = np.array([255,255,255])
        for i in range(300 - self.r - self.c, 300):
            for j in range(0, 200):
                if not self.showObstacle:
                    self.map[j, i] = 1
                else:
                    self.animationImage[j,i] = np.array([255,255,255])
        pass

    def showMap(self):
        plt.imshow(self.map, cmap="gray")
        plt.show()

    def checkFeasibility(self, node):
        h, w = node[0], node[1]
        if h >= self.H or w >= self.W or h < 0 or w < 0:
            return False
        elif self.map[h, w] == 1:
            return False
        else:
            return True

    def checkVisited(self, node):
        if self.explored[node[0], node[1]] == 1:
            return False
        else:
            return True

    def addParent(self, node, parentNode, cost):
        self.parentData[node[0], node[1],:2] = np.array(parentNode)
        self.parentData[node[0], node[1], 2] = cost
        pass

    def getParent(self, node):
        return tuple(self.parentData[node[0], node[1], :])

    def getCost(self, node):
        return self.parentData[node[0], node[1], 2]

    def addExplored(self, node):
        self.explored[node[0], node[1]] = 1
        self.animationImage[node[0], node[1], :] = np.array([0, 0, 255])
        # print(str(node) + " explored")
        return

    def path(self, d):
        # for d in data:
        self.animationImage[int(d[0]), int(d[1]), :] = np.array([0, 255, 0])
        # print("showing final")
        # plt.imshow(self.animationImage)
        # plt.show()
        return
