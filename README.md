# Important Files
- Snakeoil.py - Automated Controller to obtain bulk training data
- trainneuralnetwork.py - Creates neural network model files from training data
- nncontroller.py - Neural Network Controller
- We use Python version 2.7

# Training Process
1. Open up two terminal windows
2. Terminal 1 - Run torcs command line mode 
-- ```torcs -r ~/.torcs/config/raceman/quickrace.xml```
3. Terminal 2 - Run training controller
-- ```python Snakeoil.py -m [num recorded samples]```
-- Has been tested up to a million data samples
-- Sampling rate = 50 samples/second
4. Training output stored in ```trainingdata.csv```
-- Data Format: ```[direction, track position, speed, gear value, lidar 1, lidar 2, lidar 3, lidar 4, lidar 5, acceleration, brake, steering]```

# Neural Network Creation Process
1. Run ```python trainneuralnetwork.py```
2. Neural Network Structure
-- 9 Inputs - ```direction, track position, speed, gear value, lidar 1, lidar 2, lidar 3, lidar 4, lidar 5```
-- Layer 2 - 20 hidden nodes (relu)
-- Layer 3 - 20 hidden nodes (relu)
-- Layer 4 - 20 hidden nodes (relu)
-- Layer 5 - 20 hidden nodes (relu)
-- Output - Concatenated (```steering (tanh)```,``` acceleration (sigmoid)```)
3. Output Files
-- ```model.json``` - Architecture file
-- ```model.h5``` - Weights file

# Execution Process
1. Open two terminals
2. Terminal 1- Open Torcs Gui
-- New Race
-- Start Race
3. Terminal 2 - Run Neural Network Controller
-- ```Python nncontroller.py```
# Vehicle Simulator - TORCS 1.3.7
Source - https://github.com/fmirus/torcs-1.3.7#torcs-137
## Installation Instructions
This installation guide has been tested with Ubuntu 16.04!

### Install torcs dependencies
First we need to get some necessary debian packages

```
sudo apt-get install mesa-utils libalut-dev libvorbis-dev cmake libxrender-dev libxrender1 libxrandr-dev zlib1g-dev libpng16-dev
```
Now check for openGL/DRI by running
```
glxinfo | grep direct
```
The result should look like
```
direct rendering: Yes
```
Check for glut by running
```
dpkg -l | grep glut
```
If it is not installed run
```
sudo apt-get install freeglut3 freeglut3-dev
```
Check for libpng by running
```
dpkg -l | grep png
```
### Install PLIB
First we have to create a folder for all torcs-related stuff. Therefore, run the following commands
```
cd /your_desired_location/
```
```
sudo mkdir torcs
```
```
export TORCS_PATH=/your_desired_location/torcs
```
```
cd $TORCS_PATH
```
### Install PLIB-dependencies
```
sudo apt-get install libxmu-dev libxmu6 libxi-dev
```
Now download PLIB 1.8.5, unpack to the created directory and enter the plib folder by
```
sudo tar xfvz /path_to_downloaded_files/plib-1.8.5.tar.gz
```
```
cd plib-1.8.5
```
Before we compile plib we need need to set some environment variables
```
export CFLAGS="-fPIC"
```
```
export CPPFLAGS=$CFLAGS
```
```
export CXXFLAGS=$CFLAGS
```
Now we can configure and compile PLIB
```
./configure
```
```
make
```
```
sudo make install
```
Just for safety, wen unset our environment variables again
```
export CFLAGS=
```
```
export CPPFLAGS=
```
```
export CXXFLAGS=
```
### Install openal
let's enter our base directory again
```
cd $TORCS_PATH
```
Now we download openal 1.17.2 and unpack it
```
sudo tar xfvj /path_to_downloaded_files/openal-soft-1.17.2.tar.bz2
```
We enter the build folder and compile openal
```
cd openal-soft-1.17.2/build
```
```
sudo cmake ..
```
```
sudo make
```
```
sudo make install
```

### Install TORCS
Enter your TORCS_PATH
```
cd $TORCS_PATH
```
and clone this repository
```
git clone https://github.com/fmirus/torcs-1.3.7.git
```
Now we enter our torcs folder
```
cd torcs-1.3.7
```
Now build we build TORCS and log the output to a text-files as TORCS does not interrupt the build on errors
```
make >& error.log
```
Now open error.log with your favourite text editor and search for errors. If there are no errors you can proceed, otherwise you have to resolve.

Now we are ready to install torcs by running
```
sudo make install
```
Also install the torcs data-files by running
```
sudo make datainstall
```
If you made it this far, you can delete the TORCS_PATH variable by unset TORCS_PATH and are now ready to go. Congratulations :-)