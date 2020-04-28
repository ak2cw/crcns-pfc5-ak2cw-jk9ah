
We downloaded the data from the pfc-5 dataset for each trial. We did this by downloading each trial's folder individually from the CRCNS website. 

The data set can be found at https://crcns.org/data-sets/pfc/pfc-5/about-pfc-5, in the data directory. 
Download all the tar.gz files into the data folder and unzip them. 
cd into your version of the /Users/amrutha/crcns-pfc5-ak2cw-jk9ah folder where data, src, venv, and scripts are saved
To generate the plots and run the main code, put this into terminal: python figures.py filepath
filepath should be replaced with your file path to the data folder, for example /Users/amrutha/crcns-pfc5-ak2cw-jk9ah/data/
it needs the last slash to work. 

figures.py imports the io.py file, and has a main function that calls the functions in io.py and then generates the plots used in our presentation, which will save to the top-level folder. 