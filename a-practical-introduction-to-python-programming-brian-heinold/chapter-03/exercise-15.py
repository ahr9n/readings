# 15. Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦ in
# 15◦ increments. Each result should be rounded to 4 decimal places. Sample output is shown
# below:

# 0 --- 0.0 1.0
# 15 --- 0.2588 0.9659
# 30 --- 0.5 0.866
# ...
# 345 --- -0.2588 0.9659

import math

# Note: Trigonometric functions receive the parameters only in radian
# Now, we should convert angle from degrees to radian
# radian = degree / 180 * pi

for angle_degree in range(0, 346, 15):
    angle_radian = angle_degree / 180 * math.pi

    sine = round(math.sin(angle_radian), 4)
    cosine = round(math.cos(angle_radian), 4)

    print(angle_degree, "---", sine, cosine)
