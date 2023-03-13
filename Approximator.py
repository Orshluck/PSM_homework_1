import math
from math import factorial


class Approximator:
    def __init__(self):
        pass

    def approx(self, numberToApproximate, degreeOfApproximation,units):
        approxmatedValue = 0
        sign = 1
        degreeOfApproximation = degreeOfApproximation * 2 #i make it even, and i think this is what i intended

        if units == 'radians':
            numberToApproximate = math.degrees(numberToApproximate) ## i think i can use this library if not
            #Angle in Radians × 180°/π = Angle in Degrees
        print("before " + str(numberToApproximate))
        # I bring it to the interval 0 2pi
        while numberToApproximate > 360:
            numberToApproximate -= 360




        numberToApproximate = self.bringToInterval(numberToApproximate)
        if numberToApproximate == 1:
            return 0

        print(numberToApproximate)
        for i in range(1,degreeOfApproximation,2):
            print(i)
            approxmatedValue += sign * (numberToApproximate ** i) / factorial(i)
            sign *= -1

        return approxmatedValue
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    def bringToInterval(self,number):
        if 0 <= number < 90 :
            return number
        elif  90  <= number < 180:
            return  180 - number
        elif 180 <= number < 270:
            return number -180
        elif 270 <= number < 360:
            return 360 - number