 
## Using Packages and Channels


#### Objectives  
**Install a package** from a specific **channel**.

### What are Conda packages? (Should we keep this part?)

A conda package is a **compressed archive file** ``` (.tar.bz2) ```  that contains:

- **system-level libraries**
- Python or other **modules**
- **executable programs** and other components
- **metadata** under the info/ directory
- a collection of files that are installed directly into an install prefix

**Conda keeps track of the dependencies between packages and platforms; the conda package format is identical across platforms and operating systems.

##### Package Structure ####

All conda packages have a **specific sub-directory** structure inside the tarball file. There is a ``` bin ``` directory that contains any **binaries** for the package; a ```lib``` directory containing the relevant **library files** (i.e., the ```.py files```); and an ```info``` directory containing package **metadata**. 

As an example of Conda package structure consider the Conda package for Python 3.6 version of PyTorch targeting a 64-bit Mac OS, ```pytorch-1.1.0-py3.6_0.tar.bz2```.

```
.
├── bin
│   └── convert-caffe2-to-onnx
│   └── convert-onnx-to-caffe2
├── info
│   ├── LICENSE.txt
│   ├── about.json
│   ├── files
│   ├── git
│   ├── has_prefix.json
│   ├── hash_input.json
│   ├── index.json
│   ├── paths.json
│   ├── recipe/
│   └── test/
└── lib
    └── python3.6
        └── site-packages
            ├── caffe2/
            ├── torch/
            └── torch-1.1.0-py3.6.egg-info/
```

A complete listing of available PyTorch packages can be found on **Anaconda Cloud**.



### What are Conda channels?

**Conda packages** are downloaded from **remote channels**, which are URLs to directories containing ```conda``` packages. The ```conda``` command searches a default set of channels, and packages are **automatically downloaded and updated** from the Anaconda Cloud channels.

- ```main```: The majority of all new Anaconda, Inc. package builds are hosted here. Included in conda’s defaults channel as the top priority channel.
- ```r```: This channel is included in conda’s defaults channel.

Collectively, the **Anaconda managed channels** are referred to as the ```defaults``` channel because, unless otherwise specified, packages installed using ```conda``` will be downloaded from these channels.

####The conda-forge channel

In addition to the ```default``` channels that are managed by ```Anaconda``` Inc., there is another channel called that also has a special status. The ```Conda-Forge``` project “is a community led collection of recipes, build infrastructure and distributions for the conda package manager.”
There are a few reasons that you may wish to use the ```conda-forge``` channel instead of the ```defaults``` channel maintained by Anaconda:

 1. Packages on ```conda-forge``` may be more **up-to-date** than those on the ```defaults``` channel.  
 2. There are packages on the ```conda-forge``` channel that **aren’t available from defaults**.  
 3. You may wish to use a dependency such as ```openblas``` (from conda-forge) instead of ```mkl``` (from ```defaults```).  

### How do I install a package from a specific channel?

You can install a package from a **specific channel** into the **currently activate environment** by passing the ```--channel``` option to the ```conda install``` command as follows.
```
$ conda activate machine-learning-env
$ conda install scipy=1.6 --channel conda-forge
```

You can also install a package from a **specific channel into a named environment** (using ```--name```) or into an environment installed at a **particular prefix** (using ```--prefix```). For example, the following command installs the ```scipy``` package from the ```conda-forge``` channel into the environment called ```my-first-conda-env``` which we created earlier.

```
$ conda install scipy=1.6 --channel conda-forge --name machine-learning-env
```

This command would install tensorflow package from conda-forge channel into an environment installed into the ```env/``` sub-directory.
```
$ conda install tensorflow=1.14 --channel conda-forge --prefix ./env
```

Here is another example for ```R ``` users. The following command would install ```r-tidyverse``` package from the ```conda-forge``` channel into an environment installed into the ```env/``` sub-directory.

$ cd ~/Desktop/introduction-to-conda-for-data-scientists
$ conda install r-tidyverse=1.3 --channel conda-forge --prefix ./env

#### Channel priority

You may specify **multiple channels** for installing packages by passing the ```--channel``` argument multiple times.
```
$ conda install scipy=1.6 --channel conda-forge --channel bioconda
```

**Channel priority decreases from left to right** - the first argument has higher priority than the second. For reference, ```bioconda``` is a channel for the conda **package manager specializing in bioinformatics software**. For those interested in learning more about the Bioconda project, checkout the project’s GitHub page.

Please note that in our example, adding bioconda channel is irrelevant because ```scipy``` is no longer available on ```bioconda``` channel.

### My package isn’t available on the defaults channel! What should I do?

It may very well be the case that packages (or often more recent versions of packages!) that you need to install for your project are **not available** on the ```defaults``` channel. In this case you should try the following.

```conda-forge```: the ```conda-forge``` channel contains a **large number of community curated conda packages**. Typically the most recent versions of packages that are generally available via the ```defaults``` channel are available on conda-forge first.  
```bioconda```: the ```bioconda``` channel also contains a **large number of Bioinformatics** curated ```conda``` packages. ```bioconda``` channel is meant to be used with ```conda-forge```, you should not worried about using the two channels when installing your prefered packages.  
```pip```: only **if a package is not otherwise available** via ```conda-forge``` (or some domain-specific channel like ```bioconda```) should a package be installed into a conda environment from ```PyPI``` using ```pip```.

For example, Kaggle publishes a Python 3 API that can be used to interact with Kaggle datasets, kernels and competition submissions. You can search for the package on the ```defaults``` channels but you will not find it!
```
$ conda search kaggle

Loading channels: done
No match found for: kaggle. Search: *kaggle*

PackagesNotFoundError: The following packages are not available from current channels:

  - kaggle

Current channels:

  - https://repo.anaconda.com/pkgs/main/osx-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/free/osx-64
  - https://repo.anaconda.com/pkgs/free/noarch
  - https://repo.anaconda.com/pkgs/r/osx-64
  - https://repo.anaconda.com/pkgs/r/noarch


To search for **alternate channels** that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.
```

The official **installation instructions** suggest downloading the ```kaggle``` package using ```pip```. But since we are using conda we should check whether the package exists on at least ```conda-forge``` channel before proceeding to use ```pip```.

```
$ conda search --channel conda-forge kaggle
Loading channels: done  
Name                       Version           Build  Channel             
kaggle                         1.5.3          py27_1  conda-forge         
kaggle                         1.5.3          py36_1  conda-forge         
kaggle                         1.5.3          py37_1  conda-forge         
kaggle                         1.5.4          py27_0  conda-forge         
kaggle                         1.5.4          py36_0  conda-forge         
kaggle                         1.5.4          py37_0  conda-forge         
.
.
.
```

Or you can also check online at https://anaconda.org/conda-forge/kaggle.

Once we know that the ```kaggle``` package is available via ```conda-forge``` we can go ahead and install it.

```
$ conda install --channel conda-forge kaggle=1.5.10  --prefix ./env
```

### What actually happens when I install packages?

During the installation process, **files are extracted** into the **specified environment** (defaulting to the current environment if none is specified). Installing the files of a conda package into an environment can be thought of as changing the directory to an environment, and then downloading and extracting the package and its dependencies.

For example, when you ```conda install``` a **package that exists in a channel** and has **no dependencies**, conda does the following.

1. looks at your configured channels (in priority)  
2. reaches out to the repodata associated with your channels/platform
3. parses repodata to search for the package
once the package is found, conda pulls it down and installs

The [conda documentation][conda-install-docs] has a nice decision tree that describes the package installation process.

Installing with Conda

#### Specifying channels when installing packages

Like many projects, PyTorch has its own channel on Anaconda Cloud. This channel has several interesting packages, in particular ```pytorch``` (PyTorch core) and ```torchvision``` (datasets, transforms, and models specific to computer vision).

Create a new directory called ```my-computer-vision-project``` and then create a Python 3.6 environment in a sub-directory called ```env/``` with the two packages listed above. Also include the most recent version of ```jupyterlab``` in your environment (so you have a nice UI) and ```matplotlib``` (so you can make plots).

#### Solution (to do)
In order to create a new environment you use the conda create command as follows.

$ mkdir my-computer-vision-project
$ cd my-computer-vision-project/
$ conda create --prefix ./env --channel pytorch \
 python=3.6 \
 jupyterlab=1.0 \
 pytorch=1.1 \
 torchvision=0.3 \
 matplotlib=3.1

**Hint**: For the lazy typers: the --channel argument can also be shortened to -c, for more abbreviations, see also the Conda command reference .

#### Alternative syntax for installing packages from specific channels

There exists an **alternative syntax** for installing conda packages from specific channels that more explicitly links the channel being used to install a particular package.

```
$ conda install conda-forge::tensorflow  --prefix ./env
```


Create a new folder ```my-final-project``` in ```~/Desktop/introduction-to-conda-for-data-scientists``` and repeat the previous exercise using this alternative syntax to install ```python```, ```jupyterlab```, and ```matplotlib``` from the c```onda-forge``` channel and ```pytorc``` and ```torchvision``` from the ```pytorch``` channel.

#### Solution (to do)
One possibility would be to use the conda create command as follows.

$ cd ~/Desktop/introduction-to-conda-for-data-scientists
$ mkdir my-final-project
$ cd my-final-project/
$ conda create --prefix ./env \
 conda-forge::python=3.6 \
 conda-forge::jupyterlab=1.0 \
 conda-forge::matplotlib=3.1 \
 pytorch::pytorch=1.1 \
 pytorch::torchvision=0.3




### A Python package isn’t available on any Conda channel! What should I do?

If a Python package that you need isn’t available on any Conda channel, then you can use the default Python package manager Pip to install this package from PyPI. However, **there are a few potential issues that you should be aware of when using Pip to install Python packages when using Conda.**

First, **Pip is sometimes installed by default on operating systems where it is used to manage any Python packages needed by your OS. You do not want to use this pip to install Python packages when using Conda environments.**

```
(base) $ conda deactivate
$ which python
/usr/bin/python
$ which pip # sometimes installed as pip3
/usr/bin/pip

```

Second, Pip is also included in the Miniconda installer where it is used to install and manage OS specific Python packages required to setup your base Conda environment. **You do not want to use this pip to install Python packages when using Conda environments.**

```
$ conda activate
(base) $ which python
~/miniconda3/bin/python
$ which pip
~/miniconda3/bin/pip
```

#### Another reason to avoid installing packages into your base Conda environment

If your ```base``` Conda environment becomes cluttered with a **mix of Pip and Conda installed packages it may no longer function.** Creating separate conda environments allows you to delete and recreate environments readily so you dont have to worry about risking your core Conda functionality when mixing packages installed with Conda and Pip.

If you meed to install a Python package that **is only available via Pip**, then you should first install ```pip``` into your Conda environment and then use that ```pip``` to install the desired package. Using the ```pip``` **installed in your Conda environment to install Python packages not available via Conda channels will help you avoid difficult to debug issues that frequently arise when using Python packages installed via a pip that was not installed inside you Conda environment.**

#### Conda (+Pip): Conda wherever possible; Pip only when necessary

**When using Conda to manage environments for your Python project it is a good idea to install packages available via both Conda and Pip using Conda**; however there will always be **cases** where a **package is only available via Pip** in which case you will need to use **Pip**. Many of the common **pitfalls of using Conda and Pip together** can be avoided by adopting the following practices.

- **Always explicitly install** ```pip``` **in every Python-based Conda environment.**
- **Always be sure your desired environment is active before installing anything using pip.**
- **Prefer ```python -m pip install``` over ```pip install```; never use ```pip``` with the ```--user argumen```t.**

#### Installing packages into Conda environments using pip

Combo is a comprehensive Python toolbox for combining machine learning models and scores. Model combination can be considered as a subtask of ensemble learning, and has been widely used in real-world tasks and data science competitions like Kaggle.

Activate the ```machine-learning-env``` you created in a previous challenge and use ```pip``` to ```install``` combo.

Solution (TO DO)
The following commands will activate the basic-scipy-env and install combo.

```
$ conda install --name machine-learning-env pip
$ conda activate machine-learning-env
$ python -m pip install combo==0.1.*
```


#### Key Points

- A package is a tarball containing system-level libraries, Python or other modules, executable programs and other components, and associated metadata.

- A Conda channel is a URL to a directory containing a Conda package(s).

- Explicitly including the channels (and their priority!) in a project’s environment file is necessary for another researcher to completely re-create that project’s software environment.

- Understand how to use Conda and Pip together effectively.


#########################


## Sharing Environments


#### Objectives

- Create an environment from a YAML file that can be read by Windows, Mac OS, or Linux.

- Create an environment based on exact package versions.

- Create a custom kernel for a Conda environment for use inside JupyterLab and Jupyter notebooks.

### Working with environment files

When working on a **collaborative research project** it is often the case that **your operating system might differ from the operating systems used by your collaborators**. Similarly, the operating system used on a remote cluster to which you have access will likely differ from the operating system that you use on your local machine. In these cases it is **useful to create an operating system agnostic environment file** which you can **share** with collaborators or use to **re-create an environment** on a remote cluster.

#### Creating an environment file

In order to make sure that your **environment is truly shareable**, you need to make sure that the contents of your environment are described in such a way that the resulting environment file can be used to re-create your environment on Linux, Mac OS, and Windows. **Conda uses YAML** (“YAML Ain’t Markup Language”) **for writing its environment files**. YAML is a human-readable data-serialization language that is commonly used for configuration files and that uses Python-style indentation to indicate nesting.

Creating your project’s Conda environment from a single environment file is a **Conda “best practice”**. Not only do you have a file to share with collaborators but you also have a **file that can be placed under version control which further enhancing the reproducibility of your research project and workflow.**

#### Default environment.yml file

Note that by convention Conda environment files are called ```environment.yml```. As such if you use the ```conda env create``` sub-command **without** passing the ```--file``` option, then **conda will expect** to find a file called ```environment.yml``` in the current working directory and will throw an error if a file with that name can not be found.

Let’s take a look at a few **example** ```environment.yml``` files to give you an idea of how to write your own environment files.

```
name: machine-learning-env

dependencies:
  - ipython
  - matplotlib
  - pandas
  - pip
  - python
  - scikit-learn
```

This ```environment.yml``` file would create an environment called ```machine-learning-env``` with the most current and mutually compatible versions of the listed packages (including all required dependencies). The newly created environment would be installed inside the ```~/miniconda3/envs/``` directory, unless we specified a different path using ```--prefix```.

Since **explicit versions numbers for all packages should be preferred a better environment file** would be the following.

```
name: machine-learning-env

dependencies:
  - ipython=7.13
  - matplotlib=3.1
  - pandas=1.0
  - pip=20.0
  - python=3.6
  - scikit-learn=0.22
```

Note that we are only **specifying the major and minor version** numbers and **not the patch or build numbers**. Defining the version number by fixing only the major and minor version numbers while allowing the patch version number to vary **allows us to use our environment file to update our environment to get any bug fixes whilst still maintaining significant consistency of our Conda environment across updates.**

**Always version control your ```environment.yml``` files!**

While you should **never version control the contents of your ```env/``` environment sub-directory**, **you should always version control your ```environment.yml``` files**. **Version controlling your ```environment.yml``` files together with your project’s source code** means that you always know which versions of which packages were used to generate your results at any particular point in time.

Let’s suppose that you want to use the ```environment.yml``` file defined above to create a Conda environment in a sub-directory of some project directory. Here is how you would accomplish this task.

```
$ cd ~/Desktop/introduction-to-conda-for-data-scientists
$ mkdir project-dir
$ cd project-dir
```

Once your project folder is created, create ```environment.yml``` using your favourite editor for instance nano. Finally create a new conda environment:

```
$ conda env create --prefix ./env --file environment.yml
$ conda activate ./env
```

Note that the above sequence of commands assumes that the ```environment.yml``` file is stored within your project-dir directory.

### Automatically generate an environment.yml

To export the packages installed into the previously created ```machine-learning-env``` you can run the following command:

```
$ conda env export --name machine-learning-env 
```

When you run this command, you will see the resulting **YAML formatted representation of your Conda environment** streamed to the terminal. Recall that we only listed five packages when we originally created ```machine-learning-env``` yet from the output of the ```conda env export``` command we see that these five packages result in an environment with roughly 80 dependencies!

To export this list into an environment.yml file, you can use ```--file``` option to directly save the resulting YAML environment into a file.

```
$ conda env export --name machine-learning-env --file environment.yml
```

Make sure you do not have any other ```environment.yml``` file from before in the same directory when running the above command.

**This exported environment file will however not consistently produce environments that are reproducible across Mac OS, Windows, and Linux.** The reason is, that it may **include operating system specific low-level packages** which cannot be used by other operating systems.

**If you need an environment file that can produce environments that are reproducibile across Mac OS, Windows, and Linux, then you are better off just including those packages into the environment file that your have specifically installed.**

```
$ conda env export --name machine-learning-env --from-history --file environment.yml
```

In short: to make sure others can reproduce your environment independent of the operating system they use, make sure to add the ```--from-history``` argument to the ```conda env export``` command.

#### Create a new environment from a YAML file.

Create a new project directory and then create a new environment.yml file inside your project directory with the following contents.

```
name: scikit-learn-env

dependencies:
  - ipython=7.13
  - matplotlib=3.1
  - pandas=1.0
  - pip=20.0
  - python=3.6
  - scikit-learn=0.22
```

Now use this file to create a new Conda environment. Where is this new environment created? Using the same ```environment.yml``` file create a Conda environment as a sub-directory called env/ inside a newly created project directory. Compare the contents of the two environments.

#### Solution (to do)
To create a new environment from a YAML file use the conda env create sub-command as follows.

```
$ mkdir scikit-learn-project-dir
$ cd scikit-learn-project-dir
$ nano environment.yml
$ conda env create --file environment.yml
```

The above sequence of commands will create a new Conda environment inside the ```~/miniconda3/envs``` directory. In order to create the Conda environment inside a sub-directory of the project directory you need to pass the ```--prefix``` to the conda env create command as follows.

```
$ conda env create --file environment.yml --prefix ./env
```

You can now run the ```conda env list``` command and see that these two environments have been created in different locations but contain the same packages.

#### Specifying channels in the environment.yml

We learned in the previous episode, that some packages may need to be installed from other than the defaults channel. We can also specify the channels, that conda should look for the packages within the ```environment.yml file```:

```
name: pytorch-env

channels:
    - pytorch
    - defaults

dependencies:
  - pytorch=1.1
```

When the above file is used to create an environment, conda would first look in the ```pytorch``` channel for all packages mentioned under dependencies. If they exist in the ```pytorch``` channel, conda would install them from there, and not look for them in ```defaults``` at all.

### Updating an environment

You are unlikely to know ahead of time which packages (and version numbers!) you will need to use for your research project. For example it may be the case that:
- one of your core dependencies just released a new version (dependency version number update).
- you need an additional package for data analysis (add a new dependency).
- you have found a better visualization package and no longer need to old visualization package (add new dependency and remove old dependency).

If any of these occurs during the course of your research project, all you need to do is update the contents of your ```environment.yml``` file accordingly and then run the following command.

```
$ conda env update --prefix ./env --file environment.yml  --prune
```

Note that the ```--prune``` option tells Conda to **remove any dependencies that are no longer required from the environment**.

#### Rebuilding a Conda environment from scratch

When working with ```environment.yml``` files it is often just as **easy to rebuild the Conda environment** from scratch whenever you need to add or remove dependencies. To rebuild a Conda environment from scratch you can pass the ```--force``` option to the ```conda env create``` command which will remove any existing environment directory before rebuilding it using the provided environment file.

```
$ conda env create --prefix ./env --file environment.yml --force
```

#### Add Dask to the environment to scale up your analytics

Add ```Dask``` to the ```scikit-env``` environment file and update the environment. Dask provides advanced parallelism for data science workflows enabling performance at scale for the core Python data science tools such as Numpy Pandas, and Scikit-Learn.

#### Solution (to do)

The ```environment.yml``` file should now look as follows.

```
name: scikit-learn-env

dependencies:
  - dask=2.16
  - dask-ml=1.4
  - ipython=7.13
  - matplotlib=3.1
  - pandas=1.0
  - pip=20.0
  - python=3.6
  - scikit-learn=0.22
```
  
You could use the following command, that will **rebuild the environment from scratch** with the new Dask dependencies:

```
$ conda env create --prefix ./env --file environment.yml --force 
```
Or, if you just want to **update the environment** in-place with the new Dask dependencies, you can use:

```
$ conda env update --prefix ./env --file environment.yml  --prune
```

#### Installing via pip in environment.yml files

Since you write ```environment.yml``` files for all of your projects, you might be wondering how to specify that packages should be installed using ```pip``` in the ```environment.yml``` file. Here is an example ```environment.yml``` file that uses ```pip``` to install the ```kaggle``` and ```yellowbrick``` packages.

```
name: example

dependencies:
 - jupyterlab=1.0
 - matplotlib=3.1
 - pandas=0.24
 - scikit-learn=0.21
 - pip=19.1
 - pip:
   - kaggle==1.5
   - yellowbrick==0.9
```

Note the **double ‘==’ instead of ‘=’ for the pip installation** and that you should include ```pip``` itself as a dependency and then a subsection denoting those packages to be installed via ```pip```. 

```
$ conda install --channel conda-forge yellowbrick=1.2 --prefix ./env
```

An alternative way of installing dependencies via pip in your environment files is to store all the packages that you wish to install via pip in a requirements.txt file and then add the following to your environment.yml file.

```
...
  - pip
  - pip:
    - -r file:requirements.txt
```

Conda will then install your ```pip``` dependencies using ```python -m pip install -r requirements.txt``` (after creating the Conda environment and installing all Conda installable dependencies).


### Key Points

- Sharing Conda environments with other researchers facilitates the reprodicibility of your research.
- Create an environment.yml file that describes your project’s software environment.



