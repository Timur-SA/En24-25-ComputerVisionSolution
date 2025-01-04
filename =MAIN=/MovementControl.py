import math

class MovementController:
    accuracy = 0.1

    def MoveToTarget(self, robotCenter, robotFor, target):
        theta_r = math.atan2(robotFor[0]-robotCenter[0], robotFor[1]-robotCenter[1])
        theta_t = math.atan2(target[0]-robotCenter[0], target[1]-robotCenter[1])

        delta = theta_r - theta_t

        #!!!

        if(delta+self.accuracy > 0):
            return
        elif(delta-self.accuracy < 0):
            return
        else:
            return
