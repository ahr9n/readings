# 14. Write a program that asks the user to enter an angle in degrees and prints out the sine of that
# angle.

import math

angle_degree = eval(input("Enter an angle in degrees: "))

# Note: Trigonometric functions receive the parameters only in radian
# Now, we should convert angle from degrees to radian

# radian = degree / 180 * pi
angle_radian = angle_degree / 180 * math.pi

sine = math.sin(angle_radian)

print("Sine of ", angle_degree, "◦ is ", sine, sep="")
