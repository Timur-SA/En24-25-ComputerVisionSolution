import math

class MovementController:
    def __init__(self, accuracy=0.1):
        self.accuracy = accuracy

    def MoveToTarget(self, robotCenter, robotFor, target):
        robotDir = math.atan2(robotFor[0]-robotCenter[0], robotFor[1]-robotCenter[1])
        targDir = math.atan2(target[0]-robotCenter[0], target[1]-robotCenter[1])

        delta = robotDir - targDir

        #!!!

        if(delta+self.accuracy > 0):
            return "l"
        elif(delta-self.accuracy < 0):
            return "r"
        else:
            return "f"
