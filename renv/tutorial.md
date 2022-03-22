# Using virtual environments with R and renv

## Prerequisites

Following this tutorial requires:

- A recent (3.6.2 or higher) working version of R and/or Rstudio
- A working installation of the `renv` R package

### Installing the `renv` R package:
You can simply install the `renv`R package from CRAN, as any other regular package:
```
> install.packages('renv')
```
and then load it as usual:
```
library(renv)
```

## Tutorial

Here we will use the `renv` R package to create an environment that will allow you to run a simple R script called `brca_PCA.R`. This script uses a similar dataset as the one used in the previous example, which actually comes from the same source and which is available in the `mlbench` R package. The script loads the data, performs PCA as for the previous example and writes a scatter plot showing the projection of the samples on the first two principal components (`brca_pcs_R.png`). Please notice that the Python and R datasets are not identical for number of samples and features, meaning that you shouldn't expect exactly the same result (even though they should be reasonably similar). We will see how to build an environment that is able to run this script and install the prerequisites. Running the script requires:
 - R/Rstudio >= 3.6.2
 - the `mlbench`, `factoextra` R packages

### Preparing for the tutorial
In order to download the script you can just clone the course's GitHub repository and enter the `virtualenv` directory:
```
git clone https://github.com/ELELAB/environments_workshop.git 
cd environments_workshop/renv/brca_PCA
```
where you'll find the `brca_PCA.R` script. Read the content of the `brca_PCA.R` script and take note of what R packages are being imported

Open R or Rstudio. You will need to set this directory as your working directory if it's not already: 
```
setwd(/data/user/teo/environments_workshop/renv/brca_PCA)
```

### Initializing your environment
In order to create a new environment, just run in R/Rstudio:
```
library(renv)
renv::init()
```
the package will warn you it's about to create some files and directories. Read the warning and ultimately accept. Restart the R session if it was not done automatically (it usually is). Your environment is ready. You will notice that you no longer have access to R libraries you have installed system-wide - meaning your environment is isolated.

While running `init`, `renv` created the `renv`folder, containing your new R environment, and the `**renv.lock**` file which contains a description of your environment. It also creates a `.Rprofile` file in the project folder for the automatic discovery of the environment. 

While doing this,`renv` examined the .R files contained in your project folder, determined automatically which dependencies you need, installed them, and updated your `renv.lock` with a description of the environment. Neat! 

Notice that you can run `renv::dependencies()` independently to read the *explicit* dependencies that your project is based on.

### Running the script
You are now ready to run or source the R script:
```
source('brca_PCA.R`)
```
This will create an image file with the projections of data points the principal components. You can close R/Rstudio and reopen it for the next step.

### Activating an already existing environment
We will now try and run the script again from a fresh RStudio session. This will allow us to showcase how to reuse an environment you have already created.

By default, when you run Rstudio, no environment is active. In order to activate your recently created environment, you need to change the working directory to the one you desire:
 ```
setwd(/data/user/teo/environments_workshop/renv)
```
and then run
```
library(renv)
renv::activate()
```

You can then try running the PCA script as before:
```
source('brca_PCA.R`)
```
Notice that if you run your R/Rstudio session *starting from your project directory*,  the environment will be used automatically. This is because the environment also includes a `.Rprofile` file which is run automatically upon starting R/Rstudio.

### Modifying your environment

Once your environment is created, it will stay the same unless you specifically ask for it to be updated. First of all, modify your `brca_PCA.R` script by adding a `library` statement for a different package that is not loaded yet (for instance, `Biostrings`, a Bioconductor package) and save it. Then, you can install it by using either the usual `BiocManager::install` or the more convenient `renv::install()` function:
```
renv::install('bioc::Biostrings')
```
here notice the `bioc::` before the package name that signals `renv` that is in fact a Bioconductor package.
We than save our environment by running:

```
renv::snapshot()
```
This will write the changes in the environment to the lock file.

Please notice that, by default, *only the packages that your R code loads will be saved in the environment*. If a package has been installed manually but isn't loaded by one of your R project files it will be not considered. This behaviour can be changed before running `snapshot` by changing a setting so that it saves *all* the installed packages:
```
renv::settings$snapshot.type("all")
```

### Restoring your environment to your latest snapshot
If you want to revert you environment to the state in which it was the last time it was saved (i.e. `snapshot()` was used) you can just run:
```
renv::restore()
```
We will not demonstrate this.

### Sharing your environment
Sharing your environment with other researchers is done by sharing some of the files generated by `renv`:
* as a bare minimum, your `renv.lock`
* possibly, also the `.Rprofile` and `renv/activate.R` which are the auto-loaders for `renv`

You should share these files with other people that intend to reproduce the results of your project, e.g. by uploading them together to a GitHub repository together with the rest of it

### Reproducing someone else's environment
In order to do this you should have received someone's project (i.e. code) and their environment `renv.lock` file. We have provided an example of this in the course data (the `dplyr` directory inside `env`). 

First restart your R session. Change your current working directory to the `dplyr` project folder:
```
setwd(/data/user/teo/environments_workshop/renv/dplyr)
```
This means that the project files and the `renv.lock` are in the project folder. Then run:
```
library(renv)
env::restore()
```
Depending on whether you also have the auto-loaders files for this project (see above) you might be asked if you want to activate it. If you answer yes, the project will be activated before restoring. The end process of this is that you will now have a `env` environment very similar if not identical to the one that the one that the other researchers shared. 

