# Getting Started with Conda #
<br/>


### *Objectives* 
- Understand why you should use a package and environment management system as part of your (data) science workflow.

- Explain the benefits of using Conda as part of your (data) science workflow.


<br/>
## Packages and Environments
### Packages

Python, R, as well as many other programming languages use external libraries or packages for being able to doing complex analysis.  
  
#### Modules, packages, libraries
**Module**: a collection of functions and variables, as in a script
**Package**: a collection of modules, as in a directory with scripts  
**Library**: a collection of packages with realted functionality
Library/Package are often used interchangeably.
  
  
<br/>
### Dependencies
A bit further into your programming career you may notice/have noticed that many packages do not just do everything on their own. Instead, they depend on other packages for their functionality. 
For example, the Scipy package is used for numerical routines. To not reinvent the functionality which is already available, the package makes use of other packages, such as numpy (numerical python) and matplotlib (plotting) and many more. So we say that numpy and matplotlib are dependencies of Scipy.

Many packages are being further developed all the time, generating different **versions** of packages. During development it may happen that a function call changes and/or functionalities are added or removed. If one package can depend on another, this may create issues. Therefore it is not only important to know that e.g. Scipy depends on numpy and matplotlib, but also that it depends on numpy version >= 1.6 and matplotlib version >= 1.1. Numpy version 1.5 in this case would not be sufficient.


<br/>
### Environments
In some of the workflows, one version of a package or also the programming language might not be enough anymore. You may find an older tool that depends on an older version of your programming language (e.g. Pyhton 2.7), but many of your other tools depend on a newer version (e.g. Python 3.6). You could now start up another computer or virtual machine to run the other version of the programming language, but this is not very handy, since you may want to use the tools together in a workflow later on. Here, environments are one solution to the problem. Nowadays there are several environment management systems following a similar idea: Instead of having to use multiple computers or virtual machines to run different versions of the same package, you can install packages in isolated environments.


<br/>
### Environment management
An environment management system solves a number of **problems commonly encountered by (data) scientists.**  

**Examples:**

- An application you need for a research **project requires different versions of your base programming language or different versions of various third-party packages** from the versions that you are currently using.
- **Code that have written for a joint research project works on your machine but not on your collaborators’ machines.**
- **An application that you are developing on your local machine doesn’t provide the same results when run on your remote cluster.**  

An environment management system enables you to set up a new, project specific software environment containing specific Python/R/etc. versions as well as the versions of additional packages and required dependencies that are all mutually compatible.

- Environment management systems help **resolve dependency issues by allowing you to use different versions of a package for different projects.**
- Make your **projects self-contained and reproducible by capturing all package dependencies in a single requirements file.**
- Allow you to install packages on a host on which **you do not have admin privileges.**


## Package management
A good package management system greatly simplifies the process of installing software by:

1) identifying and installing **compatible versions** of software and all required dependencies.
2) handling the process of **updating software** as more recent versions become available.  

If you use some flavor of Linux, then you are probably familiar with the package manager for your Linux distribution (i.e., **apt on Ubuntu, yum on CentOS**); if you are a **Mac OSX** user then you might be familiar with the **Home Brew** Project which brings a Linux-like package management system to Mac OS; if you are a Windows OS user, then you may not be terribly familiar with package managers as **there isn’t really a standard package manager for Windows** (although there is the Chocolatey Project).

Operating system package management tools are great but these tools actually solve a more general problem than you often face as a (data) scientist. As a (data) scientist you typically use one or two core scripting languages (i.e., Python, R, SQL). Each scripting language has **multiple versions that can potentially be installed and each scripting language will also have a large number of third-party packages** that will need to be installed. The exact version of your core scripting language(s) and additional, third-party packages will also probably change from project to project.


## Why should I use a package and environment management system?
Installing software is hard. Installing scientific software is often even more challenging. In order to minimize the burden of installing and updating software (data) scientists often install software packages that they need for their various projects system-wide.

**Installing software system-wide has a number of drawbacks:**

- It can be difficult to figure out what software is required for any particular research project.
- **It is often impossible to install different versions of the same software package at the same time.**
- **Updating software** required for one project can often **“break”** the software installed for another project.  

Put differently, installing software system-wide creates complex dependencies between your research projects that shouldn’t really exist!

Rather than installing software system-wide, wouldn’t it be great if we could install software separately for each research project?


<br/>
## Conda
From the [official Conda documentation](https://conda.io/projects/conda/en/latest/index.html) - Conda is an **open source package and environment management system** that runs on Windows, Mac OS and Linux.

- Conda can **quickly install, run, and update packages and their dependencies.**
- Conda can **create, save, load, and switch** between project specific software environments on your local computer.
- Although Conda was created for **Python** programs, Conda can package and distribute software for any language such as **R, Ruby, Lua, Scala, Java, JavaScript, C, C++, FORTRAN.**  

Conda as a package manager **helps you find and install packages**. If you need a package that requires a different version of Python, you do not need to switch to a different environment manager, because Conda is also an environment manager. With just a few commands, you can set up a totally separate environment to run that different version of Python, while continuing to run your usual version of Python in your normal (system) environment.  


<br/>
### Conda vs. Miniconda vs. Anaconda

![alt text](https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/fig/miniconda_vs_anaconda.png)

 Miniconda combines Conda with Python and a small number of core packages; Anaconda includes Miniconda as well as a large number of the most widely used Python packages.


<br/>
### Why use Conda?
Whilst there are many different **package and environment management** systems that solve either the package management problem or the environment management problem, **Conda solves both of these problems** and explicitly targeted at (data) science use cases.

- Conda **provides prebuilt packages, avoiding the need to deal with compilers**, or trying to work out how exactly to set up a specific tool. 
- Conda is cross platform, with support for Windows, MacOS, GNU/Linux, and support for multiple hardware platforms, such as x86 and Power 8 and 9. 
- **Conda environments are reproducible** (reproducibility being one of the major issues facing science), and Conda allows you to provide your environment to other people across these different platforms.
- **Conda allows for using other package management tools** (such as pip) inside Conda environments, where a library or tools is not already packaged for Conda.
- Additionally, Anaconda provides commonly used data science libraries and tools, such as R, NumPy, SciPy and TensorFlow built using optimised, hardware specific libraries (such as Intel’s MKL or NVIDIA’s CUDA), which provides a speedup without having to change any of your code.


<br/>
### Key Points
- Conda is a platform agnostic, open source package and environment management system.

- Using a package and environment management tool facilitates portability and reproducibility of (data) science workflows.

- Conda solves both the package and environment management problems and targets multiple programming languages. Other open source tools solve either one or the other, or target only a particular programming language.

- Anaconda is compatible with many programming languages




</br></br>
# Working with Environments  


### *Objectives* 
Understand how Conda environments can improve your research workflow.

Create a new environment.

Activate (deactivate) a particular environment.

Install packages into existing environments using Conda (+pip).

Specify the installation location of an environment.

List all of the existing environments on your machine.

List all of the installed packages within a particular environment.

Delete an entire environment.  


</br>
Create a new introduction-to-conda-for-data-scientists directory on your Desktop in order to maintain a consistent workspace for all your conda environment.
</br>  
</br>  


All the commands will be run from **bash** terminal.
```
$ cd ~/Desktop #cd ~\Desktop for Windows users
$ mkdir introduction-to-conda-for-data-scientists
$ cd introduction-to-conda-for-data-scientists
```


## What is a Conda environment

A Conda environment is a **directory that contains a specific collection of Conda packages** that you have installed. Conda environment might be specific for each project. **If you change one environment, the other environments are not affected.** You can easily activate or deactivate environments, which is how you switch between them.

##### Avoid installing packages into your base Conda environment

Conda has a default environment called **"base"** that include a **Python installation and some core system libraries and dependencies of Conda.** It is a **“best practice”** to avoid installing additional packages into your base software environment. **Additional packages** needed for a new project should always be installed into a **newly created Conda environment.**



## Creating environments
To create a new environment for Python development using conda you can use the conda create command.

```
$ conda create --name python3-env python
```

It is a good idea to give your environment a meaningful name in order to help yourself remember the purpose of the environment. While naming things can be difficult, **$PROJECT_NAME-env** is a good convention to follow. To make your results more reproducible it's recommended to provide **specific version** of a package why you had to create a new environment.

```
$ conda create --name python36-env python=3.6
```

You can use search to see what versions of the package are available using the conda search command.

```
$ conda search $PACKAGE_NAME
```

You can create a Conda environment and install multiple packages by listing the packages that you wish to install.

```
$ conda create --name basic-scipy-env ipython=7.13 matplotlib=3.1 numpy=1.18 scipy=1.4
```

When conda installs a package into an environment it also **installs all the required dependencies.** For example, even though Python is not listed as a package to install into the basic-scipy-env environment above, conda will still install Python into the environment because it is a required dependency of at least one of the listed packages.

</br>
#### Creating a new environment
Create a new environment called “machine-learning-env” with Python and the most current versions of IPython, Matplotlib, Pandas, Numba and Scikit-Learn.

</br>
<details>
  <summary>Solution</summary>

    ```
    $ conda create --name machine-learning-env
     ipython 
     matplotlib
     pandas 
     python 
     scikit-learn 
     numba
    ```
</details>


</br>
## Activating an existing environment
Activating environments is essential to making the software in environments work well (or sometimes at all!). Activation of an environment does two things.

1) Adds **environment PATH to the system PATH.**  
2) Runs activation scripts that the environment may contain (**setting up arbitrary environment variables that may be necessary for their operation**).

You activate the basic-scipy-env environment by name using the activate command.

```
$ conda activate basic-scipy-env
```
You can see that an environment has been activated because the shell prompt will now include the name of the active environment.

```
(basic-scipy-env) $
```

</br>
## Deactivate the current environment

To deactivate the currently active environment use the Conda ```deactivate``` command as follows.

```
(basic-scipy-env) $ conda deactivate
```

You can see that an environment has been deactivated because the shell prompt will no longer include the name of the previously active environment.

```
$
```

</br>
#### Returning to the base environment ####

To return to the ```base``` Conda environment, it’s better to call ```conda activate``` with no environment specified, rather than to use ```deactivate```. If you run ```conda deactivate``` from your ```base``` environment, you may lose the ability to run ```conda``` commands at all. Don’t worry if you encounter this undesirable state! Just start a new shell.


</br>
#### Activate an existing environment by name
Activate the machine-learning-env environment created in the previous challenge by name.


<details>
  <summary>Solution</summary>
  
    ```
    conda activate machine-learning-env
    ```
  
</details>


</br>
## Installing a package into an existing environment

You can install a package into an existing environment using the ```conda install``` command. This command accepts a list of package specifications (i.e., numpy=1.18) and **installs a set of packages consistent with those specifications and compatible with the underlying environment. If full compatibility cannot be assured, an error is reported and the environment is not changed.**

By default the ```conda install``` command will **install packages into the current, active environment.** The following would activate the basic-scipy-env we created above and install Numba, an open source JIT compiler that translates a subset of Python and NumPy code into fast machine code, into the active environment.

```
$ conda activate basic-scipy-env
$ conda install numba
```

As was the case when listing packages to install when using the ```conda create``` command, if version numbers are not explicitly provided, Conda will **attempt to install the newest versions of any requested packages.** To accomplish this, **Conda may need to update some packages** that are already installed or install additional packages. It is always a **good idea to explicitly provide version numbers** when installing packages with the conda install command. For example, the following would install a particular version of Scikit-Learn, into the current, active environment.

```
$ conda install scikit-learn=0.22
```

</br>
#### Freezing installed packages
**To prevent existing packages from being updating** when using the conda install command, you can use the ```--freeze-installed``` option. This may force Conda to install older versions of the requested packages in order to maintain compatibility with previously installed packages. Using the ```--freeze-installed``` option does not prevent additional dependency packages from being installed.

</br>
#### Installing a package into a specific environment
Dask provides advanced parallelism for data science workflows enabling performance at scale for the core Python data science tools such as Numpy Pandas, and Scikit-Learn. Have a read through the official documentation for the conda install command and see if you can figure out how to install Dask into the machine-learning-env that you created in the previous challenge.

<details>
  <summary>Solution</summary>
</br>
    You can install Dask into machine-learning-env using the conda install command as follow.  
  ```
  $ conda install --name machine-learning-env dask=2.16
  ```
</br>
    You could also install Dask into machine-learning-env by first activating that environment and then using the conda install command.  
    ```
    $ conda activate machine-learning-env  
    ```
</br>
    ```
    $ conda install dask=2020.12
    ```
</details>


</br>
## Where do Conda environments live?
Environments created with conda, by default, live in the envs/ folder of your miniconda3 (or anaconda3) directory the absolute path to which will look something the following: ```/Users/$USERNAME/miniconda3/envs``` or ```C:\Users\$USERNAME\Anaconda3```.  

Running ``ls`` (linux) / ``dir`` (Windows) on your conda ``envs/`` directory will list out the directories containing the existing Conda environments.


</br>
## How do I specify a location for a Conda environment?
You can control where a Conda environment lives by providing a **path to a target directory when creating the environment**. For example to following command will create a new environment in a sub-directory of the current working directory called env.

```
$ conda create --prefix ./env ipython=7.13 matplotlib=3.1 pandas=1.0 python=3.6
```

You activate an environment created with a **prefix** using the same command used to activate environments created by name.

```
$ conda activate ./env
```

**It is often a good idea to specify a path to a sub-directory of your project directory when creating an environment**. Why?

Makes it easy to tell if your project utilizes an isolated environment by including the environment as a sub-directory.
**Makes your project more self-contained as everything including the required software is contained in a single project directory**.
An additional benefit of creating your project’s environment inside a sub-directory is that you can then **use the same name for all your environments**; if you keep all of your environments in your ```~/miniconda3/env/``` folder, you’ll have to give each of them a different name.


#### Creating a new environment as a sub-directory within a project directory
First create a project directory called project-dir using the following command.

```
$ mkdir project-dir
$ cd project-dir
```
Next, create a new environment inside the newly created project-dir in a sub-directory called env an install Python 3.6, version 3.1 of Matplotlib, and version 2.0 of TensorFlow.

<details>
  <summary>Solution</summary>
</br>
project-dir $ conda create --prefix ./env 
python=3.6
matplotlib=3.1 
tensorflow=2.0 
</details>
 
</br>
**Placing Conda environments outside of the default ```~/miniconda3/envs/``` folder** comes with a couple of minor drawbacks.   
**First, ```conda``` can no longer find your environment with the ```--name``` flag**; you’ll generally need to pass the ```--prefix``` flag along with the environment’s full path to find the environment.  
**Second**, an annoying side-effect of specifying an install path when creating your Conda environments is that your command prompt is now prefixed with the active environment’s **absolute path** rather than the environment’s name. After activating an environment using its prefix your prompt will look similar to the following.

```
(/absolute/path/to/env) $
```


This could be fixed by running the command below (will create/edit ```~/.condarc``` configuration file and display only environment name): 

```
$ conda config --set env_prompt '({name})'
```

```
$ cd project-directory
$ conda activate ./env
(env) project-directory $
```

#### Activate an existing environment by path
Activate the environment created in a previous challenge using the path to the environment directory.

<details>
  <summary>Solution</summary>
</br>
You can activate an existing environment by providing the path the the environment directory instead of the environment name when using the ```conda activate``` command as follows.  

```$ conda activate ./env```
</br>
Note that the provided path can either be absolute or relative. If the path is a relative path then it must start with ./ on Unix systems and .\ when using PowerShell on Windows.

</details>


</br>
#### Conda can create environments for R projects
First create a project directory called r-project-dir using the following command.

```
$ cd ~/Desktop/introduction-to-conda-for-data-scientists
$ mkdir r-project-dir
$ cd r-project-dir
```

Next, take a look through the list of R packages available by default for installation using ```conda```. Create a new environment inside the newly created r-project-dir in a sub-directory called ```env``` and install ```r-base```, ```r-tidyverse``` and ```r-sparklyr```.

<details>
  <summary>Solution</summary>
</br>
project-dir $ conda create --prefix ./env r-base r-tidyverse r-sparklyr

</details>


## Listing existing environments
Now that you have created a number of Conda environments on your local machine. In case you have forgotten the names of all of the environments and exactly where they live, there is a ```conda``` command to list all of your existing environments together with their locations.

```
$ conda env list
```

## Listing the contents of an environment
There is a ```conda``` command for listing the contents on an environment. To list the contents of the ```basic-scipy-env``` that you created above, run the following command.

```
$ conda list --name basic-scipy-env
```

If you created your Conda environment using the ```--prefix``` option to install packages into a particular directory, then you will need to use that prefix in order for conda to locate the environment on your machine.

```
$ conda list --prefix /path/to/conda-env
```

#### Listing the contents of a particular environment.
List the packages installed in the ```machine-learning-env``` environment that you created in a previous challenge.

<details>
  <summary>Solution</summary>
</br>
You can list the packages and their versions installed in ```machine-learning-env``` using the ```conda list``` command as follows.  

```$ conda list --name machine-learning-env```
</br>

To list the packages and their versions installed in the active environment leave off the ```--name``` or ```--prefix``` option.  

```$ conda list```
</details>


## Deleting entire environments
Occasionally, you will want to delete an entire environment. Perhaps you were experimenting with conda commands and you created an environment you have no intention of using; perhaps you no longer need an existing environment and just want to get rid of cruft on your machine. Whatever the reason, the command to delete an environment is the following.

```
$ conda remove --name my-first-conda-env --all
```

If you wish to delete and environment that you created with a ```--prefix``` option, then you will need to provide the prefix again when removing the environment.

```
$ conda remove --prefix /path/to/conda-env/ --all
```

#### Delete an entire environment
Delete the entire “basic-scipy-env” environment.

<details>
  <summary>Solution</summary>
In order to delete an entire environment you use the conda remove command as follows.  
    
```
$ conda remove --name basic-scipy-env --all --yes
```
</br>
This command will remove all packages from the named environment before removing the environment itself. The use of the --yes flag short-circuits the confirmation prompt (and should be used with caution).
</details>


## Key Points
- A Conda environment is a directory that contains a specific collection of Conda packages that you have installed.

- You create (remove) a new environment using the ```conda create``` (```conda remove```) commands.

- You activate (deactivate) an environment using the ```conda activate``` (```conda deactivate```) commands.

- You install packages into environments using ```conda install```; you install packages into an active environment using ```pip install```.

- You should install each environment as a sub-directory inside its corresponding project directory

- Use the ```conda env list``` command to list existing environments and their respective locations.

- Use the ```conda list``` command to list all of the packages installed in an environment.