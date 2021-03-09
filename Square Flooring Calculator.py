#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
# Code suggestion by Doug McNally
# Author:      s-sargupta
#
# Created:     10/04/2017
# Copyright:   (c) s-sargupta 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def areaSquare(length, width):
    area = length * width

    if area > 200:
        print("You will need more flooring")

    else:
        print("You have enough flooring")


areaSquare(10,20)