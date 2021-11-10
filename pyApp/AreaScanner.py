import math


class AreaScanner:

    def __init__(self, res, lines, szw, szh):
        self.lines = lines
        self.res = res
        self.szw = szw
        self.szh = szh

    def hydrateWp(self):
        pos = []
        for y in range(self.lines+1):
            for x in range(self.res):
                if(y % 2 == 0):
                    xPos = self.szw/self.res * x - self.szw/2
                else:
                    xPos = self.szw/self.res * (self.res-x) - self.szw/2

                yPos = self.szh/self.lines * y - self.szh/2

                pos.append([xPos, yPos])
        return pos
