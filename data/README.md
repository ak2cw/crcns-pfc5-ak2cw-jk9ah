
Edit this file to describe how to retrieve the data set. Except for very small data files, it's not recommended to check data into version control.
We downloaded the data from the pfc-5 dataset for each trial and kept the .mat file. We renamed all the files to data_derived#.mat. We did this by downloading each file individually from the CRCNS website. 

The data set can be found at https://crcns.org/data-sets/pfc/pfc-5/about-pfc-5, in the data directory. 
Download all the tar.gz files into the data folder and unzip them. 
When you run the src io.py file, put this into terminal: python io.py filepath
filepath should be replaced with your file path to the data folder, for example /Users/amrutha/crcns-pfc5-ak2cw-jk9ah/data/
it needs the last slash to work. This will run the code for generating all of our graphs, they will save to the src folder. 