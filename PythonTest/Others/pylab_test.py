# coding=utf-8

import pylab as pl
import random


if __name__ == '__main__':
    x = range(25)
    y = [random.randint(0, 100) for i in range(25)]

    pl.plot(
        x, y,
        marker='o',  # type of point
        linestyle=':',  # type of line: -, --, -., :
        linewidth=2,
        markerfacecolor='m',  # color of point
        color='b',  # color of line
        label='233'
    )
    pl.legend(loc='upper left')  # position of label: upper/lower left/right
    pl.axis([0, 25, -10, 110])  # [x_min, x_max, y_min, y_max]
    pl.xlabel('data_x')
    pl.ylabel('data_y')
    pl.title('233_test')
    pl.show()
