#How do I go about this? Do I model the problem as is or do I try to solve it?

import numpy as np

class p151:

	def __init__(self):
		self.job = 0
		self.reqd_answer = 0
		self.counts = [1,0,0,0,0]
		self.counts_map = ['A1', 'A2', 'A3', 'A4', 'A5']

	def get_sheets(self):
		sheets = list()
		for i in range(5):
			papertype = self.counts_map[i]
			for j in range(self.counts[i]):
				sheets.append(papertype)
		return sheets

	def calc_number_of_sheets(self):
		sum = 0
		for i in self.counts:
			sum += i
		return sum

	def divide_sheet(self, selected_sheet):
		index = self.counts_map.index(selected_sheet)
		self.counts[index] -= 1
		for i in range(index + 1, 5):
			self.counts[i] += 1
		self.job += 1

	def main_job(self):
		#Contains the number of A0,A1,A2..A5 pieces available
		while self.job < 17:
			number_of_sheets = self.calc_number_of_sheets()
			if number_of_sheets == 0:
				break
			available_sheets = self.get_sheets()
			if number_of_sheets == 1:
				self.reqd_answer += 1
			selected_index = np.random.randint(0,number_of_sheets)
			selected_sheet = available_sheets[selected_index]
			if selected_sheet == 'A5':
				self.counts[4] -= 1
				self.job += 1
			else:
				self.divide_sheet(selected_sheet)
			print self.counts
		return self.reqd_answer