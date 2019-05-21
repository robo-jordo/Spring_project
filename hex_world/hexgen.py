#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import time

class HexGrid:
	def __init__(self, n):
		self.n = n
		self.c = []
		self.x = []
		self.y = []
		add = 3
		if (self.n%2!=0):
			add = 2
		for i in range(self.n):
			for j in range(self.n):
				self.x.append(i)
				self.y.append(j)
				self.c.append(1)
		self.X = np.array(self.x)
		self.Y = np.array(self.y)

		self.xmin = self.X.min()
		self.xmax = self.X.max()
		self.ymin = self.Y.min()
		self.ymax = self.Y.max()

	def draw(self):
		self.fig, self.axs = plt.subplots(ncols=1)
		self.ax = self.axs
		self.hb = self.ax.hexbin(self.X, self.Y, C=self.c, gridsize=8, cmap='inferno', edgecolors='white')
		self.ax.axis([0, 9, 0, 9])
		self.ax.set_title("Hexagon binning")
		self.fig.canvas.draw()

		plt.ion()
		plt.show()
		plt.pause(0.01)
		plt.ioff()

		

	def place(self,index):

		self.c[index] = self.c[index] + 20
		self.new_hexbin = self.ax.hexbin(self.X, self.Y, C=self.c, gridsize=8, cmap='inferno', edgecolors='white')
		self.ax.axis([self.xmin, self.xmax, self.ymin, self.ymax])
		self.ax.set_title("Hexagon binning")
		self.hb.update_from(self.new_hexbin)
		self.fig.canvas.draw()
	# update the viewed hexbin from the new one
		plt.ion()
		plt.show()
		plt.pause(0.01)
		plt.ioff()

world1 = HexGrid(9)
world1.draw()

num = 0
while(1):
	num = num + 1
	time.sleep(0.05)
	world1.place(num)
	if num>60:
		num = 0




