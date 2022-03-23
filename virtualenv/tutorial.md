# Using virtual environments with Python and virtualenv

## Prerequisites

Following this tutorial requires:

- Access to a Linux terminal (e.g. on your computer, through `ssh`, or using the Windows Subsystem for Linux)
 - A working installation of Python, >=2.7
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
git clone https://github.com/ELELAB/environments_workshop.git
cd environments_workshop/virtualenv
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
If you have prepared the environment correctly, this should run the script and generate the `brca_pcs_py.png` without errors. Notice that the Python interpreter we are using is not the system-wide one, it is the one included in the environment.

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

### Saving the state of your environment
`pip` and virtualenv have a way to save the state of your repository (i.e. which packages are installed and their versions) so that each environment can

 - be easily reconstructed from scratch, so one doesn't need to keep the environment around at all times
 - be reconstructed by another researcher to reproduce your environment
 - be more version-aware

This is done by using the command `pip freeze`, which prints a list of all the installed packages and their versions:
```
$ pip freeze > requirements.txt
```
For instance, the content of the `requirements.txt` file for our example is:
```
cycler==0.11.0
fonttools==4.29.1
joblib==1.1.0
kiwisolver==1.3.2
matplotlib==3.5.1
numpy==1.21.5
packaging==21.3
pandas==1.3.5
Pillow==9.0.1
pkg_resources==0.0.0
pyparsing==3.0.7
python-dateutil==2.8.2
pytz==2021.3
scikit-learn==1.0.2
scipy==1.7.3
six==1.16.0
sklearn==0.0
threadpoolctl==3.1.0
```
Notice that:
- `requirements.txt` is the standard name for this type of environment file, however it can be called in any way 
- the output includes both the packages you have installed explicitly as well as those that were installed as requirements of other packages
- all the packages have version numbers, even though we did not require specific versions when they were installed
- here the `requirements.txt` file was generated automatically, however you can create from scratch or edit by hand such a file, just [respecting the file format](https://pip.pypa.io/en/stable/cli/pip_install/#requirement-specifiers). For instance, Packages are not required to have an explicit version number (in that case the latest version is considered), or their version can be specified using other qualifiers such as `>=`, `>`, `<`... . It is also possible to explicitly require the installation of a package from a specific web resource, e.g. a GitHub repository, specifying the clone target and a commit ID (in case a specific commit is desired):
 ```
git+https://github.com/ELELAB/mutatex.git@44eed08c3b73a186abf702e7a53fd05a2d5568fe
```
### Deactivating your environment
In order to deactivate your environment you just need to run:
```
$ deactivate
```

### Reproducing your environment
With a `requirements.txt` files in hand, it is very easy to reproduce an environment. It can be done, in a new and clean environment, using a single command. For instance, you can deactivate and remove your environment:

```
$ deactivate
$ rm -rf env
```

and then re-create it just by :

```
$ virtualenv -p python3.7 env
$ source env/bin/activate
$ pip install -r requirements.txt
```
the environment can then be used as-is or modified as required.
