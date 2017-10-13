import resampling
import math
import sys

if len(sys.argv) != 5:
	print ('Incorrect Format!')
	print ('python resampling_run.py filename num_data num_runs run_name')

else:
	filename = sys.argv[1]
	num_data = int(sys.argv[2])
	num_runs = int(sys.argv[3])
	run_name = sys.argv[4]

	resampled = resampling.Resample()
	resampled.num_data = num_data
	resampled.num_runs = num_runs


	resampled.import_file(filename)
	output_list = []
	for i in range(0,num_runs):
		resampled.separate_list(i,output_list)
		print(run_name,"[",i,"]:")
		resampled.resample(output_list, 500, 1000)
		#print("Sample std_dev =", resampled.sample_std_dev(output_list))
		#print("Sample_mean =",resampled.sample_mean(output_list))
		#print("Output_List =", output_list)
		#resample output_list
		#sample mean
		#std_dev
		#confidence_interval
