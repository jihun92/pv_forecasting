import matplotlib.pyplot as plt
import numpy as np

class linearRegression:

    s1 = 0
    s2 = 0

    def h(self, x):
        return self.s1 + self.s2*x

    def j(self, x, y):
        if x.size != y.size:
            raise Exception('not same size x between y')
        m = x.size
        result = 0
        for i in range(0, m):
            result += (self.h(x[i])-y[i])**2
        result = 1/2*m*result
        return result

if __name__ == '__main__':

    x = np.array([2104,1416,1534,852]);
    y = np.array([460,232,315,178]);

    lr = linearRegression()
    lr.j(x,y)
    # rs = lr.j(s1, s2, x[0], y[0])
    # print("error: {0} \t y: {1} \t y': {2}".format(rs, y[0], lr.h(s1, s2, x[0])))
