import math


class AreaScanner:

    def __init__(self, wpList, res, lines):
        self.wpList = wpList
        self.lines = lines
        self.res = res

    def hydrateWp(self):
        pos = []
        for y in range(self.lines+1):
            for x in range(self.res):
                if(y % 2 == 0):
                    xPos = 40/self.res * x - 20
                else:
                    xPos = 40/self.res * (self.res-x) - 20

                yPos = 40/self.lines * y - 20

                pos.append([xPos, yPos])
        return pos
