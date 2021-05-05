import matplotlib.pyplot as plt
import pandas as pd
from os import listdir

# Absolute path of the working directory
working_directory = '/media/pi/disk/'

# Test filename for testing purposes.
#filename = 'TEK00000.CSV'

# Function to find csv files.
def find_files():
	file_set = set()

	# Iterate through files in the working directory.
	for filename in listdir(working_directory):

		# Add the filename to set() if *.csv extension.
		# Side effect: adds a null entry of 'working_directory' that needs to be discarded later.
		file_set.add(working_directory + filename.lower().endswith('csv') * filename)

	# Discard the null entry.
	file_set.discard(working_directory)

	# return the set of csv files
	return file_set

# Function to parse the csv files into Pandas Data Frames.
def read_csv():
	# pull the csv files as a set()
	csv_files = find_files()

	# setup some variables
	pd_dict = {}
	i = 0

	# iterate through each file in the set()
	for csv_file in csv_files:
		# Use Pandas to read each csv file and store the Data Frame in an iterated dictionary
		pd_dict[i] = pd.read_csv(csv_file,names = ['time','voltage'])
		# iterate the dictionary counter
		i += 1
	return pd_dict

# Function to plot the Pandas Data Frames in the same manner as an Oscope.
def plot_csv():
	# Pull the Pandas Data Frames as a dictionary{}
	data_frames = read_csv()

	# Iterate through the dictionary{} of Data Frames.
	for k in data_frames:
		# Plot each Data Frame separately. Assigning the x-axis and y-axis as it is on the Oscope.
		data_frames[k].plot(x='time',y='voltage')

	# Display all of the plots.
	plt.show()

if __name__ == "__main__":
	print("executed directly as main")
	plot_csv()
