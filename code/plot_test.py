import matplotlib.pyplot as plt
import numpy as np

class linearRegression:

    def h(self, s1, s2, x):
        return s1+s2*x

    def j(self, s1, s2, x, y):
        lr = linearRegression()
        m = x.size
        rs = 0
        for i in range(0, m):
            rs += (lr.h(s1, s2, x)-y)**2
        rs = 1/2*m*rs
        return rs

if __name__ == '__main__':

    x = np.array([2104,1416,1534,852]);
    y = np.array([460,232,315,178]);

    lr = linearRegression()
    s1 = 1
    s2 = 0.5
    rs = lr.j(s1, s2, x[0], y[0])
    print("error: {0} \t y: {1} \t y': {2}".format(rs, y[0], lr.h(s1, s2, x[0])))
