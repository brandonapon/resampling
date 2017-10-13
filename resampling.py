import math
from random import randint

class Resample:
	def __init__(self):
		self.input_data = []
		self.num_runs = 0
		self.num_data = 0
		self.conf_50 = 0.67449
		self.conf_90 = 1.64485

	def import_file(self, filename):
		#reads in .txt file and saves bin values
		file = open(filename, "r")
		data = file.read().split()
		for i in data:
			self.input_data.append(int(i))
		index_full = 0
		#print ("Self.input_bins =", self.input_data)

	def separate_list(self, num_run, run_list):
		#returns run_list with nums from num_run
		del run_list[:]
		j = 0
		while j < self.num_data:
			run_list.append(self.input_data[self.num_runs*j+num_run])
			j+=1

	def sample(self, data_list, sample_size):
		temp_list = []
		for i in range(0,sample_size):
			temp_list.append(data_list[randint(0,len(data_list)-1)]) 
		return self.sample_mean(temp_list)

	def resample(self, data_list, resample_runs, sample_size):
		list_of_means = []
		for runs in range(resample_runs):
			list_of_means.append(self.sample(data_list,sample_size))
		resample_mean = self.sample_mean(list_of_means)
		resample_std_dev = self.sample_std_dev(list_of_means)
		print("Resample_Mean =", resample_mean)
		print("Resample_Std_Dev =", resample_std_dev)
		self.confidence_intervals(resample_mean, resample_std_dev, sample_size, 50)
		self.confidence_intervals(resample_mean, resample_std_dev, sample_size, 90)


	def sample_mean(self, run_list):
		total = 0
		for num in run_list:
			total += num
		return float(total/(len(run_list)))

	def sample_std_dev(self, run_list):
		orig_sample_mean = self.sample_mean(run_list)
		modified_list = []
		for i in range(0,(len(run_list))):
			modified_list.append(pow((run_list[i]-orig_sample_mean),2))
		square_mean = self.sample_mean(modified_list)
		return math.sqrt(square_mean)

	def confidence_intervals(self, mean, std_dev, sample_size, z):
		#prints confidence interval
		if z == 50:
			print("Confidence Interval 50% = (", mean-(self.conf_50*(std_dev/math.sqrt(sample_size))), ",", mean+(self.conf_50*(std_dev/math.sqrt(sample_size))),")")
		else:
			print("Confidence Interval 90% = (", mean-(self.conf_90*(std_dev/math.sqrt(sample_size))), ",", mean+(self.conf_90*(std_dev/math.sqrt(sample_size))),")")