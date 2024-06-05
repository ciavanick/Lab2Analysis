# Analysis

bad code to do the analysis.

To run the code first upload the txt files for the Calibration in the `CalData` folder, after this set the `setup.py` file with your calibration txt files names and the value of tour input times and their errors (y and ye).

After this you have to upload in the `Data` folder the data acquisition txt file.

Now you can run the `run.sh` bash script for the complete analysis, just type:


`bash run.sh name_of_your_data_acquisition_file.txt`


or 

`chmod +x run.sh
./run.sh name_of_your_data_acquisition_file.txt`



Note: there can be be some errors.
