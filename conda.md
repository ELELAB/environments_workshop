
# Using firtual environments with Conda

## Prerequisites

Following this tutorial requires:

- Access to a Linux terminal (e.g. on your computer, through `ssh`, or using the Windows Subsystem for Linux)
- A working installation of conda/**miniconda**/anaconda

```
conda -h
```

</br>
**Latest miniconda installer links are available here**:
https://docs.conda.io/en/latest/miniconda.html

</br>
## Tutorial

Here we will use Conda to create an environment that will allow you to run a simple Python script called brca_PCA.py available in ```environments_workshop/conda``` (the same file used in the previous python virtualenv section).

Running the script requires:
 - Python >=3.7 
 - The following Python packages
	 - matplotlib
	 - pandas
	 - scikit-learn (sklearn)

</br>
### Preparing for the tutorial

Create a project folder inside of ```environments_workshop/conda/``` called ```introduction-to-conda```.
</br>  


All the commands will be run from **bash** terminal.
```
mkdir ./conda/introduction-to-conda
cd ./conda/introduction-to-conda
```


## What is a Conda environment
A Conda environment is a **directory that contains a specific collection of Conda packages** that you have installed. Conda environment might be specific for each project. **If you change one environment, the other environments are not affected.** You can easily activate or deactivate environments, which is how you switch between them.


## Creating environments
To create a new environment for Python development using conda you can use the ```conda create``` command.

**Preferably**, conda environment should be created in the **project folder** and using specific program/tool version (**if not specified, most recent version will be installed**):

```
conda create --prefix ./env python=3.7
```

This makes it easy to tell if your project utilizes an isolated environment by including the environment as a sub-directory.
**Makes your project more self-contained as everything including the required software is contained in a single project directory**.
An additional benefit of creating your project’s environment inside a sub-directory is that you can then **use the same name for all your environments**.  


</br>
You can use **search** to see what versions of the package are available using the conda search command.

```
conda search $PACKAGE_NAME
```

You can create a Conda environment and install multiple packages by listing the packages that you wish to install.

```
conda create --prefix ./env python=3.7 matplotlib=3.5.1 pandas=1.3.5 
```

When conda installs a package into an environment it also **installs all the required dependencies.** For example, even though Python is not listed as a package to install into the ```introduction-to-conda``` environment above, conda will still install Python into the environment because it is a required dependency of at least one of the listed packages.

</br>
#### Excercise - Creating a new environment
Create a new project called “conda-excercise-1” with conda environment including Python and the most current versions of matplotlib, pandas and scikit-learn.

</br>
<details>
  <summary>Solution</summary>

    ```
    mkdir ./conda-excercise-1  
    cd ./conda-excercise-1  
    conda create --prefix ./env matplotlib pandas scikit-learn
    ```
</details>


</br>
## Activating an existing environment
Activating environments is essential to making the software in environments work well.

We activate the environment ```env``` in ```introduction-to-conda``` project by name using the activate command. In case environment was created using ```--prefix``` option, we define absolute or relative path the the environment. After the activation, all the necessary packages became available for running our python script.

```
cd ./introduction-to-conda
conda activate ./env
```

You can see that an environment has been activated because the shell prompt will now include the name of the active environment.

```
(env) $
```

</br>
Let's run our script

```
python ../brca_PCA.py
```
</br>
## Deactivate the current environment

To deactivate the currently active environment use the Conda ```deactivate``` command as follows.

```
(env) $ conda deactivate
```

You can see that an environment has been deactivated because the shell prompt will no longer include the name of the previously active environment.


</br>
#### Returning to the base environment ####

To return to the ```base``` Conda environment (might be also "miniconda3"), it’s better to call ```conda activate``` with no environment specified, rather than to use ```deactivate```. If you run ```conda deactivate``` from your ```base``` environment, you may lose the ability to run ```conda``` commands at all. Don’t worry if you encounter this undesirable state! Just start a new shell.


</br>
#### Excercise - Activate an existing environment using path to env and running brca_PCA.py
Activate the environment ```env``` in ```conda-excercise-1``` project created in the previous excercise, run the brca_PCA.py and deactivate the environment.


<details>
  <summary>Solution</summary>
  
    ```
    conda activate ./conda-excercise-1/env
    python ../brca_PCA.py
    conda deactivate
    ```
  
</details>


</br>
## Installing a package into an existing environment

You can install a package into an existing environment using the ```conda install``` command. This command accepts a list of package specifications (i.e., scikit-learn=1.0.2) and **installs a set of packages consistent with those specifications and compatible with the underlying environment. If full compatibility cannot be assured, an error is reported and the environment is not changed.**

By default the ```conda install``` command will **install packages into the current, active environment.** The following would activate the ```introduction-to-conda``` we created above and install ```scikit-learn```.

```
conda activate ./introduction-to-conda/env
conda install scikit-learn
```

If version numbers are not explicitly provided, Conda will **attempt to install the newest versions of any requested packages.** To accomplish this, **Conda may need to update some packages** that are already installed or install additional packages. It is always a **good idea to explicitly provide version numbers** when installing packages with the conda install command. For example, the following would install a particular version of Scikit-Learn, into the current, active environment.

```
conda install scikit-learn=1.0.2
```

</br>
##### Avoid installing packages into your base Conda environment

Conda has a default environment called **"base"** that include a **Python installation and some core system libraries and dependencies of Conda.** It is a **“best practice”** to avoid installing additional packages into your base software environment. **Additional packages** needed for a new project should always be installed into a **newly created Conda environment.**


</br>
#### Excercise - Installing a package into a specific environment
Dask provides advanced parallelism for data science workflows enabling performance at scale for the core Python data science tools such as Numpy, Pandas, and Scikit-Learn. Have a read through the official documentation for the conda install command and see if you can figure out how to install Dask into the ```conda-excercise-1``` project conda environment that you created in the previous challenge.

<details>
  <summary>Solution</summary>
</br>
    You could install ```dask=2022.2.1``` into conda-excercise-1 environment by first activating that environment and then using the conda install command.  
    ```
    conda activate ./conda-excercise-1/env
    ```
</br>
    ```
    conda install dask=2022.2.1
    ```
</details>



</br>
#### Conda can create environments for R projects
First create a project directory called r-project-dir using the following command.

```
mkdir ./r-project-dir
cd ./r-project-dir
```

Excercise - Create a new environment inside the newly created r-project-dir in a sub-directory called ```env``` and install ```r-base```, ```r-tidyverse``` and ```r-sparklyr```.

```
conda create --prefix ./env r-base r-tidyverse r-sparklyr
```


## Listing existing environments
Now that you have created a number of Conda environments on your local machine. In case you have forgotten the names of all of the environments and exactly where they live, there is a ```conda``` command to list all of your existing environments together with their locations.

```
conda env list
```

## Listing the contents of an environment
There is a ```conda``` command for listing the contents on an environment. To list the contents of the environment in the ```introduction-to-conda``` project that you created above, run the following command.

```
cd ./introduction-to-conda
conda list --prefix ./env
```

#### Excercise - Listing the contents of a particular environment.
List the packages installed in the ```conda-excercise-1/env``` environment that you created in a previous challenge.

<details>
  <summary>Solution</summary>
</br>
You can list the packages and their versions installed in ```./conda-excercise-1/env``` using the ```conda list``` command as follows.  

```conda list --prefix ./conda-excercise-1/env```
</br>
</details>


## Deleting entire environments
Occasionally, you will want to delete an entire environment. Perhaps you were experimenting with conda commands and you created an environment you have no intention of using; perhaps you no longer need an existing environment and just want to get rid of cruft on your machine. Whatever the reason, the command to delete an environment is the following.


If you wish to delete and environment that you created with a ```--prefix``` option, then you will need to provide the prefix again when removing the environment.

```
conda remove --prefix r-project-dir/env --all
```


#### Excercise - Delete the entire “r-project-dir/env” environment.

<details>
  <summary>Solution</summary>
In order to delete an entire environment you use the conda remove command as follows.  
    
```
$ conda remove --prefix ./conda-excercise-1/env --all --yes
```
</br>
This command will remove all packages from the named environment before removing the environment itself. The use of the --yes flag short-circuits the confirmation prompt (and should be used with caution).
</details>




## Tips and tricks
**Optionally**, we can use ```--name``` instead of ```--prefix```.

```
$ conda create --name python3-env python=3.7
```

This will create ```python3-env``` environment into /home/$USER/.conda/envs/

It is a good idea to give your environment a meaningful name in order to help yourself remember the purpose of the environment. While naming things can be difficult, **$PROJECT_NAME-env** is a good convention to follow. 

</br>
## Using Packages and Channels


</br>
### What are Conda channels?

**Conda packages** are downloaded from **remote channels**, which are URLs to directories containing ```conda``` packages. The ```conda``` command searches a default set of channels, and packages are **automatically downloaded and updated** from the Anaconda Cloud channels.

- ```main```: The majority of all new Anaconda, Inc. package builds are hosted here. Included in conda’s defaults channel as the top priority channel.
- ```r```: This channel is included in conda’s defaults channel.

Collectively, the **Anaconda managed channels** are referred to as the ```defaults``` channel because, unless otherwise specified, packages installed using ```conda``` will be downloaded from these channels.

</br>
#### The conda-forge channel

In addition to the ```default``` channels that are managed by ```Anaconda``` Inc., there is another channel called that also has a special status. The ```Conda-Forge``` project “is a community led collection of recipes, build infrastructure and distributions for the conda package manager.”
There are a few reasons that you may wish to use the ```conda-forge``` channel instead of the ```defaults``` channel maintained by Anaconda:

 1. Packages on ```conda-forge``` may be more **up-to-date** than those on the ```defaults``` channel.  
 2. There are packages on the ```conda-forge``` channel that **aren’t available from defaults**.  

</br>
### How do I install a package from a specific channel?

You can install a package from a **specific channel** into the **currently activate environment** by passing the ```--channel``` option to the ```conda install``` command as follows.

```
conda activate ./introduction-to-conda/env
conda install scipy=1.7.3 --channel conda-forge
```


</br>
#### Channel priority

You may specify **multiple channels** for installing packages by passing the ```--channel``` or ```-c``` argument multiple times.

```
conda install scipy=1.7.3 --channel conda-forge --channel bioconda
```

**Channel priority decreases from left to right** - the first argument has higher priority than the second. For reference, ```bioconda``` is a channel for the conda **package manager specializing in bioinformatics software**.


</br>
### My package isn’t available on the defaults channel! What should I do?

It may very well be the case that packages (or often more recent versions of packages!) that you need to install for your project are **not available** on the ```defaults``` channel. In this case you should try the following.

```conda-forge```: the ```conda-forge``` channel contains a **large number of community curated up-to-date conda packages**.  
```bioconda```: the ```bioconda``` channel also contains a **large number of Bioinformatics** curated ```conda``` packages. ```bioconda``` channel is meant to be used with ```conda-forge```, you should not worried about using the two channels when installing your prefered packages.  
```pip```: only **if a package is not otherwise available** via ```conda-forge``` (or some domain-specific channel like ```bioconda```) should a package be installed into a conda environment from ```PyPI``` using ```pip```.

For example ```bwa```, we can search for the package on the ```defaults``` channels but you will not find it!


```
conda search bwa

```
So we can try to search it on ```bioconda``` channel.
```
conda search bwa --channel bioconda
```

```
conda install --channel bioconda bwa=0.7.17
```


</br>
### A Python package isn’t available on any Conda channel! What should I do?

If you meed to install a Python package that **is only available via Pip**, then you should first install ```pip``` into your Conda environment and then use that ```pip``` to install the desired package. Using the ```pip``` **installed in your Conda environment to install Python packages not available via Conda channels will help you avoid difficult to debug issues that frequently arise when using Python packages installed via a pip that was not installed inside you Conda environment.**


</br>


</br>
## Sharing Environments


</br>
### Working with environment files

When working on a **collaborative research project** it is often the case that **your operating system might differ from the operating systems used by your collaborators**. Similarly, the operating system used on a remote cluster to which you have access will likely differ from the operating system that you use on your local machine. In these cases it is **useful to create an operating system agnostic environment file** which you can **share** with collaborators or use to **re-create an environment** on a remote cluster.

</br>
#### Creating an environment file

In order to make sure that your **environment is truly shareable**, you need to make sure that the contents of your environment are described in such a way that the resulting environment file can be used to re-create your environment on Linux, Mac OS, and Windows. **Conda uses YAML** format **for writing its environment files**. YAML is a **human-readable** language that is commonly used for configuration files.

Creating your project’s Conda environment from a single environment file is a **Conda “best practice”**. Not only do you have a file to share with collaborators but you also have a **file that can be placed under version control which further enhancing the reproducibility of your research project and workflow.**

</br>
#### Default environment.yml file

Note that by convention Conda environment files are called ```environment.yml```. As such if you use the ```conda env create``` sub-command **without** passing the ```--file``` option, then **conda will expect** to find a file called ```environment.yml``` in the current working directory and will throw an error if a file with that name can not be found.

Let’s take a look at a few **example** ```environment.yml``` files to give you an idea of how to write your own environment files.

```
name: env

dependencies:
  - matplotlib
  - pandas
  - scikit-learn
```

This ```environment.yml``` file would create an environment called ```env``` with the most current and mutually compatible versions of the listed packages (including all required dependencies). 

Since **explicit versions numbers for all packages should be preferred a better environment file** would be the following.

```
name: env

dependencies:
  - matplotlib=3.5.1 
  - pandas=1.3.5
  - scikit-learn=1.0.2
```

</br>
Note that we are only **specifying the major and minor version** numbers and **not the patch or build numbers**. Defining the version number by fixing only the major and minor version numbers while allowing the patch version number to vary **allows us to use our environment file to update our environment to get any bug fixes whilst still maintaining significant consistency of our Conda environment across updates.**

**Always version control your ```environment.yml``` files!**

While you should **never version control the contents of your ```env/``` environment sub-directory**, **you should always version control your ```environment.yml``` files**. **Version controlling your ```environment.yml``` files together with your project’s source code** means that you always know which versions of which packages were used to generate your results at any particular point in time.

Let’s suppose that you want to use the ```environment.yml``` file defined above to create a Conda environment in a sub-directory of some project directory. Here is how you would accomplish this task.

```
mkdir ./use-yml-project
cd ./use-yml-project
```

Once your project folder is created, create ```environment.yml``` using your favourite editor for instance nano. 

```
name: env

dependencies:
  - matplotlib=3.5.1 
  - pandas=1.3.5
  - scikit-learn=1.0.2
```

Finally create a new conda environment:

```
conda env create --prefix ./env --file environment.yml
conda activate ./env
```

Note that the above sequence of commands assumes that the ```environment.yml``` file is stored within your project-dir directory.


</br>
### Automatically generate an environment.yml

To export the packages installed into the previously created ```./use-yml-project/env``` you can run the following command:

```
conda env export 
```

When you run this command, you will see the resulting **YAML formatted representation of your Conda environment** streamed to the terminal. Recall that we only listed five packages when we originally created ```./use-yml-project/env``` yet from the output of the ```conda env export``` command we see that these five packages result in an environment with roughly 60 dependencies!

To export this list into an environment.yml file, you can use ```--file``` option to directly save the resulting YAML environment into a file.

```
conda env export --file environment.yml
```

Make sure you do not have any other ```environment.yml``` file from before in the same directory when running the above command.

**This exported environment file will however not consistently produce environments that are reproducible across Mac OS, Windows, and Linux.** The reason is, that it may **include operating system specific low-level packages** which cannot be used by other operating systems.

**If you need an environment file that can produce environments that are reproducibile across Mac OS, Windows, and Linux, then you are better off just including those packages into the environment file that your have specifically installed.**

```
conda env export --from-history --file environment.yml
```

In short: to make sure others can reproduce your environment independent of the operating system they use, make sure to add the ```--from-history``` argument to the ```conda env export``` command.

#### Excercise - Create a new environment from a YAML file.

Create a new project directory and then create a new environment.yml file inside your project directory with the following contents.

```
name: env

dependencies:
  - matplotlib=3.5.1 
  - pandas=1.3.5
  - scikit-learn=1.0.2
```

Now use this ```environment.yml``` to create a new Conda environment. 

#### Solution
<details>
  <summary>Solution</summary>
    
To create a new environment from a YAML file use the conda env create sub-command as follows.  


```
mkdir scikit-learn-project-dir
cd scikit-learn-project-dir
nano environment.yml
conda env create --file environment.yml --prefix ./env
```  

</details>


#### Specifying channels in the environment.yml

We learned in the previous episode, that some packages may need to be installed from other than the defaults channel. We can also specify the channels, that conda should look for the packages within the ```environment.yml file```:

```
name: env

channels:
    - bioconda
    - defaults
    
dependencies:
  - matplotlib=3.5.1 
  - pandas=1.3.5
  - scikit-learn=1.0.2
```

When the above file is used to create an environment, conda would first look in the ```bioconda``` channel for all packages mentioned under dependencies. If they exist in the ```bioconda``` channel, conda would install them from there, and not look for them in ```defaults``` at all.

</br>
### Updating an environment

You are unlikely to know ahead of time which packages (and version numbers!) you will need to use for your research project. For example it may be the case that:
- one of your core dependencies just released a new version (dependency version number update).
- you need an additional package for data analysis (add a new dependency).
- you have found a better visualization package and no longer need to old visualization package (add new dependency and remove old dependency).

If any of these occurs during the course of your research project, all you need to do is update the contents of your ```environment.yml``` file accordingly and then run the following command.

```
conda env update --prefix ./env --file environment.yml  --prune
```

Note that the ```--prune``` option tells Conda to **remove any dependencies that are no longer required from the environment**.

#### Rebuilding a Conda environment from scratch

When working with ```environment.yml``` files it is often just as **easy to rebuild the Conda environment** from scratch whenever you need to add or remove dependencies. To rebuild a Conda environment from scratch you can pass the ```--force``` option to the ```conda env create``` command which will remove any existing environment directory before rebuilding it using the provided environment file.

```
conda env create --prefix ./env --file environment.yml --force
```

#### Excercise - Add Dask to the environment to scale up your analytics

Add ```Dask``` to the ```scikit-learn-project-dir``` environment file and update the environment. Dask provides advanced parallelism for data science workflows enabling performance at scale for the core Python data science tools such as Numpy Pandas, and Scikit-Learn.

#### Solution
<details>
  <summary>Solution</summary>
    
The ```environment.yml``` file should now look as follows.  

```
name: scikit-learn-env  
  
dependencies:
  - matplotlib=3.5.1 
  - pandas=1.3.5
  - scikit-learn=1.0.2
```
</details>
  
You could use the following command, that will **rebuild the environment from scratch** with the new Dask dependencies:

```
conda env create --prefix ./env --file environment.yml --force 
```
Or, if you just want to **update the environment** in-place with the new Dask dependencies, you can use:

```
$ conda env update --prefix ./env --file environment.yml  --prune
```

</br>
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
