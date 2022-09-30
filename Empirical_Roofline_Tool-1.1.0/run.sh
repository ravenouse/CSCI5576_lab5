#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=24
#SBATCH --time=00:20:00
#SBATCH --partition=shas-testing
#SBATCH --output=ex01-%j.out

module purge
module load intel
module load impi

module load python/3.6.5

#  This "use" command is required for all of the module loads that follow:

module use /projects/scru5660/public/software/module

# To run our own, new version of valgrind:

module load valgrind-intel

# To run lstopo:

module load hwloc

# To run gnuplot:

module load gnuplot

# To run kcachegrind:
 
module load kcachegrind

# To run Intel Advisor

module use /projects/scru5660/public/software/module

ml intel_advisor



# Run the application
./ert Config/config.lab_05.01