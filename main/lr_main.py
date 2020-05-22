import sys
import pathlib
currentPath = pathlib.Path().absolute()
sys.path.append(str(currentPath)+"\\lib")

# print(str(currentPath)+"\\lib")

from linearRegression import *

lr = linearRegression()

lr.x = 1
lr.y = 0.5

print(lr.h(10))

# (1)?

# lr.s1 = 1
# lr.s2 = 0.5
