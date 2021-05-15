import matplotlib.pyplot as plt
import pandas as pd
from os import listdir

# Absolute path of the default directory for 3.5in floppy drive on RasPi
default_directory = '/media/pi/disk/'

# Test filename for testing purposes.
#filename = 'TEK00000.CSV'

# Function to find csv files.
#		Takes string of absolute path for the directory as input.
#		Returns a set of the csv files in the working directory.
def find_files(working_directory = default_directory):
	# Instantiate empty set() to store filenames in.
	file_set = set()

	# Iterate through the files in the working directory.
	for filename in listdir(working_directory):

		# Adds filename to the set() if *.csv extension.
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

	# instantiate empty list to store Data Frames in.
	pd_list = []

	# iterate through each file in the set()
	for csv_file in csv_files:
		# Use Pandas to read each csv file and store the Data Frame in a list.
		pd_list.append(pd.read_csv(csv_file,names = ['time','voltage']))
	return pd_list

# Function to plot the Pandas Data Frames in the same manner as an Oscope.
def plot_csv():
	# Pull the Pandas Data Frames as a list[]
	data_frames = read_csv()

	# Iterate through the list[] of Data Frames.
	for data_frame in data_frames:
		# Plot each Data Frame separately. Assigning the x-axis and y-axis as it is on the Oscope.
		data_frame.plot(x='time',y='voltage')

	# Display all of the plots.
	plt.show()

if __name__ == "__main__":
	print("executed directly as main")
	plot_csv()
