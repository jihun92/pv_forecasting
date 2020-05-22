import matplotlib.pyplot as plt
import numpy as np

class linearRegression:

    theta0 = 0
    theta1 = 0
    alpha = 0.05 # leaning rate
    iterations = 100

    def h(self, x):
        return self.theta0 + self.theta1*x

    def j(self, x, y):
        if x.size != y.size:
            raise Exception('not same size x between y')
        m = x.size
        cost = 0
        for i in range(m-1):
            cost += (self.h(x[i])-y[i])**2
        cost = 1/2*m*cost
        return cost

    def gradient_descent(self, x, y):
        theta_history = np.zeros((self.iterations, 2))
        if x.size != y.size:
            raise Exception('not same size x between y')

        m = x.size
        for it in range(self.iterations):
            tmp1, tmp2 = 0, 0
            for i in range(m-1):
                tmp1 += (self.h(x[i]) - y[i])
                tmp2 += (self.h(x[i]) - y[i])*x[i]

            self.theta0 = self.theta0 - self.alpha*1/m*tmp1
            self.theta1 = self.theta1 - self.alpha*1/m*tmp2

            print('{0}\ttheta0:{1}\ttheta1:{2}\tcost:{3}'.format(it, self.theta0, self.theta1, self.j(x,y)))
            # theta_history[it] = np.array(self.theta0, self.theta1)
            # print(self.j(x,y))


if __name__ == '__main__':

    # x = np.array(([2104, 1600, 2400, 1416, 3000, 1985, 1534, 1427, 1380, 1494, 1940, 2000, 1890, 4478, 1268, 1437]));
    # y = np.array(([3999, 3299, 3690, 2320, 5399, 2999, 3149, 1989, 2120, 2425, 2399, 3470, 3299, 6999, 2599, 4499]));
    x = np.array(([1.,2.,3.,4.,5.]))
    y = np.array(([1.,2.,3.,4.,5.]))
    lr = linearRegression()

    lr.gradient_descent(x,y)

    print(lr.j(x,y))
