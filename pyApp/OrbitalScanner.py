import math


class OrbitalScanner:
    def __init__(self, robot, pot, step, rad, orbSubDiv, dirVec):
        self.step = step
        self.rad = rad
        self.pot = pot
        self.dirVec = dirVec
        self.robot = robot
        self.orbSubDiv = orbSubDiv
        self.nextWp = [robot.x + dirVec[0]*step, robot.y + dirVec[1]*step]
        self.state = 0
        self.highestPot = [0, 0, 0]  # [Pot.value, posX, posY]
        self.orbitHp = [0, 0, 0]
        self.radialCenterHP = 0
        self.radialCenter = [0, 0]
        self.orbitWP = []
        self.orbitWPId = 0

        self.debugFlag = True

    def update(self):
        if self.state == 0:
            if(self.highestPot[0] < self.pot.value([self.robot.x, self.robot.y])):
                self.highestPot = [self.pot.value(
                    [self.robot.x, self.robot.y]), self.robot.x, self.robot.y]
                self.radialCenter = [self.robot.x, self.robot.y]
                self.radialCenterHP = self.pot.value(
                    [self.robot.x, self.robot.y])
                self.nextWp = [self.robot.x + self.dirVec[0]
                               * self.step, self.robot.y + self.dirVec[1]*self.step]

            else:
                if self.debugFlag:
                    self.state = 1
                # self.debugFlag = False
        elif self.state == 1:
            self.computeOrbitWP()
            self.state = 2
            self.highestPot = [0, self.robot.x, self.robot.y]
            self.orbitWPId = 0

        elif self.state == 2:

            # if(self.highestPot[0] <= self.pot.value([self.robot.x, self.robot.y])):
            #     self.orbitWPId += 1
            #     self.nextWp = self.orbitWP[self.orbitWPId]
            #     self.highestPot = [self.pot.value(
            #         [self.robot.x, self.robot.y]), self.robot.x, self.robot.y]
            # else:
            #     print(self.highestPot)
            #     self.state = 0
            #     self.highestPot = [0, self.robot.x, self.robot.y]
            #     self.nextWp = self.radialCenter
            #     self.computeNewVecDir()

            # if(self.orbitWPId >= self.orbSubDiv-1):
            #     self.orbitWPId = self.orbSubDiv-1

            self.orbitWPId += 1
            self.nextWp = self.orbitWP[self.orbitWPId]

            if(self.highestPot[0] <= self.pot.value([self.robot.x, self.robot.y])):
                self.highestPot = [self.pot.value(
                    [self.robot.x, self.robot.y]), self.robot.x, self.robot.y]
            else:
                if(self.highestPot[0] >= self.radialCenterHP):
                    self.highestPot = [0, self.robot.x, self.robot.y]
                    self.state = 0
                    self.nextWp = self.radialCenter
                    self.computeNewVecDir()

            if(self.orbitWPId >= self.orbSubDiv-1):
                print("epi center found", self.radialCenter, self.radialCenterHP)
                self.state = 3
                self.nextWp = self.radialCenter

            self.orbitHp = self.highestPot

    def computeOrbitWP(self):
        self.orbitWP = []
        for i in range(self.orbSubDiv):
            wpX = math.cos(((math.pi*2)/self.orbSubDiv)*i) * \
                self.rad + self.radialCenter[0]
            wpY = math.sin(((math.pi*2)/self.orbSubDiv)*i) * \
                self.rad + self.radialCenter[1]
            self.orbitWP.append([wpX, wpY])

    def computeNewVecDir(self):
        self.dirVec[0] = self.orbitHp[1]-self.radialCenter[0]
        self.dirVec[1] = self.orbitHp[2]-self.radialCenter[1]
        d = math.sqrt(math.pow(self.dirVec[0], 2)+math.pow(self.dirVec[1], 2))
        self.dirVec[0] /= d
        self.dirVec[1] /= d
