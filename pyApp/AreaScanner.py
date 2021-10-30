class AreaScanner:
  def __init__(self, robot, wpManager, res, lines):
    self.robot = robot
    self.wpManager = wpManager
    self.lines = lines
    self.res = res

  def hydrateWp():
    pos = []
    for y in lines:
      for x in res:
        if(Math.mod(y, 2) == 0) :
          xPos = 40/res * x 
        else :
          xPos = 40/res * (res-x)

        yPos = 40/lines * y
      pos.append([xPos, yPos])


