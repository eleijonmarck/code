#! /usr/bin/env/python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import click

@click.command()
@click.option('--name', prompt='Your name please', help='Enter your name here.')
def main(name):
    t = np.arange(0,2*np.pi, 0.1)
    x = 16*np.sin(t)**3
    y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    plt.title(name + ' we love you',fontsize = 27)
    plt.xlabel('Love')
    plt.ylabel('Love')
    plt.plot(x,y)
    plt.show()

if __name__ == '__main__':
    main()
