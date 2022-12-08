# Dijkstra MPI
Implementation of the Dijkstra algorithm serially and in parallel for the college at the Faculty of informatics and digital technologies.

Studenti:
- Rene Frlan
- Antonio Janach

### Basic instructions for using the algorithm
The instructions were created for using the algorithm on the Linux operating system. 

First, it is necessary to create a virtual environment for Python inside the directory where the code was downloaded. In the shell of the system, go to the directory where the code was downloaded (using cd command) and run the command shown below. We are doing this to prevent system Python installation from anomalies.
```sh
$ python3 -m venv env
```

Then we need to install all necessary modules to run the program. And this is done in the following way: 
```sh
pip install -r zahtjevi.txt
```

After creating a virtual environment for Python and installing all necessary modules, the code can be run. Instructions for performing the sequential Dijkstra algorithm and the parallel Dijkstra algorithm are shown below

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