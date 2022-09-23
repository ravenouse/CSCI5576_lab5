#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=00:05:00
#SBATCH --partition=shas-testing
#SBATCH --output=ex01-%j.out


# Load the modules
module purge
module load intel
module load impi 

# Run the application
python /projects/zhwa3087/CSCI5576/cs-roofline-toolkit/Empirical_Roofline_Tool-1.1.0/ert \
/projects/zhwa3087/CSCI5576/cs-roofline-toolkit/Empirical_Roofline_Tool-1.1.0/Config/config.lab_05.01