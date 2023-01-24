# Dijkstra MPI
Implementation of the Dijkstra algorithm serially and in parallel for the college at the Faculty of informatics and digital technologies.

Students:
- Rene Frlan
- Antonio Janach

## Basic instructions for using the algorithm
The instructions were created for using the algorithm on the Linux operating system. 

First, you gotta make a virtual environment for Python in the folder where you downloaded the code. Go to that folder using the "cd" command in the command prompt and run the command below. This is to keep anomalies from happening to the Python that's already on your computer.
```sh
$ python3 -m venv env
```

Then we need to install all necessary modules to run the program. And this is done in the following way:
```sh
pip install -r zahtjevi.txt
```

Upon creating a virtual environment for Python and installing all required modules, the code can be executed. The instructions for implementing the sequential version of the Dijkstra algorithm and the parallel version of the Dijkstra algorithm are outlined below.

Running the sequential Dijkstra algorithm:
```sh
python3 dijkstra-sequential.py
```

Running the parallel Dijkstra algorithm, where n denotes the number of processors:
```sh
mpiexec -n 2 python dijkstra-parallel.py
```

> In case the system does not recognize the mpiexec command, it is necessary to download and install the mpich package.
```sh
sudo apt update -y
sudo apt install mpich -y
```
