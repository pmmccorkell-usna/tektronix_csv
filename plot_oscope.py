import matplotlib.pyplot as plt
# import matplotlib.cbook as cbook
import pandas as pd
from os import listdir

# Path of the working directory
working_directory = '/media/pi/disk/'

# Test filename for testing purposes.
#filename = 'TEK00000.CSV'

def find_files():
	file_set = set()
	for filename in listdir(working_directory):
		
		# Add the filename to set() if *.csv extension.
		# Adds a null entry of 'working_directory' that needs to be discarded later.
		file_set.add(working_directory + filename.lower().endswith('csv') * filename)
		
	# Discard the null entry.
	file_set.discard(working_directory)
	
	# return the set of csv files
	return file_set

def read_csv():
	csv_files = find_files()
	pd_dict = {}
	i = 0
	for csv_file in csv_files:
		pd_dict[i] = pd.read_csv(csv_file,names = ['x','y'])
		i += 1
	return pd_dict

def plot_csv():
	data_frames = read_csv()
	for i in data_frames:
		data_frames[i].plot(x='x',y='y')
	plt.show()

plot_csv()


