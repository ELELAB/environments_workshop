# Using virtual environments with Python and virtualenv

## Prerequisites

Following this tutorial requires:

- Access to a Linux terminal (e.g. on your computer, through `ssh`, or using the Windows Subsystem for Linux)
 - A working installation of Python, 2.7+
 - Having the `virtualenv` package installed in your Python distribution. 

### Installing the `virtualenv` Python package:
You can find out if you have this package already by running:
```
$ python -m virtualenv
```
if you don't have it, your output will be something like:

```
$ python -m virtualenv
/usr/bin/python: No module named virtualenv
```

In that case you can install it using `pip` (more on this later):
```
pip install virtualenv --user
```

## Tutorial


Here we will use the `virtualenv` package to create an environment that will allow you to run a simple Python script called `brca_PCA.py`. The script uses the Wisconsin breast cancer dataset, a [freely available dataset on breast cancer diagnostic data](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29). They describe features of nuclei from an imaging experiment of tumor samples, classified into benign and malignant samples. The script loads the data, performs some subsetting and centering/rescaling, performs principal component analysis (PCA) and writes a scatter plot showing the projection of the samples on the first two principal components (`brca_pcs_py.png`). We will see how to build an environment that is able to run this script and install the prerequisites. Running the script requires:
 - Python >=3.7 
 - The following Python packages
	 - matplotlib
	 - pandas
	 - scikit-learn (sklearn)

### Preparing for the tutorial
In order to download the script you can just clone the course's GitHub repository and enter the `virtualenv` directory:
```
git clone https://github....
cd whatever/virtualenv
```
 where you'll find the `brca_PCA.py` script.

### Creating an environment using virtualenv
First we will create a Python virtual environment using `virtualenv`:
```
$ virtualenv -p python3.7 env
```
This creates a `env` folder in the current directory which contains the virtual environment, call `env`. Virtual environments can have any name. The option `-p` allows to specify which Python version or executable the environment should use. If nothing is specified, it uses the system default. *Notice that the Python version you intend to use must be already installed in your system.*

### Creating an environment using virtualenv
First we will create a Python virtual environment using `virtualenv`:
```
$ virtualenv -p python3.7 env
```
This creates a `env` folder in the current directory which contains the virtual environment, call `env`. Virtual environments can have any name. The option `-p` allows to specify which Python version or executable the environment should use. If nothing is specified, it uses the system default. *Notice that the Python version you intend to use must be already installed in your system.*

### Activating the environment
We then need to activate the environment we created:
```
$ source env/bin/activate
```
The command prompt will change to something like:
```
(env) teo@kb-bioinfo01:test_envs$
```
this shows that the environment is active

### Using pip to install packages
`pip` is the standard package handling system in Python. It relies on an oline package repository from the [Python Packages index](https://pypi.org) to download packages. Using `pip` within an environment allows to install packages that will reside exclusively in the environment and that will not available outside of it. Likewise, when an environment is active, none of the packages installed system-wide will be available. 

To install a package we can simply run:

`$ pip install packagename`

This command installs the *latest* version of package `packagename` and all its requirements. So for instance, for our case:
```
pip install matplotlib pandas sklearn
```
Notice that `pip` installs all the requirements of the packages that we are trying to install.

### Running the Python script
just run:
```
$ python brca_PCA.py
```
If you have prepared the environment correctly, this should run the script and generate the `brca_pcs_py.png` without errors.

### Deactivating the environment
In order to deactivate the environment, just run `deactivate`:
```
$ deactivate
```
Your environment will persist and be able to be used again

### `pip` commands, tips and tricks
- If we need (which we don't in this case) we can also specify package versions when installing:
```
pip install matplotlib==2.0.0
```
- `pip install --upgrade packagename` upgrades a package to the latest available version. Notice that each package can be installed only once and so only one specific version is in general available
- `pip list` shows the list of installed packages
- `pip show packagename` shows information on single installed packages, including requirements
- `pip uninstall packagename` does the opposite of `install` and removes packages from the environment. It has the same syntax. Notice that this command doesn't do any check on whether the package you are trying to remove is required by another; this means that other packages might stop working if you uninstall the wrong one. 
- `pip check` checks the consistency of the environment, i.e. if all packages have all satisfied requirements. If not, `pip` will print messages that will help understand what packages are missing

### Reproducing your environment
There is a general mechanism to 
