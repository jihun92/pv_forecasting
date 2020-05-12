import sys
import pathlib
currentPath = pathlib.Path().absolute()
sys.path.append(str(currentPath)+"\\lib")

# print(str(currentPath)+"\\lib")

import linearRegression as lr

lr.h(1)

# (1)?

# lr.s1 = 1
# lr.s2 = 0.5
