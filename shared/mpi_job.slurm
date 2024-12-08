#!/bin/bash
#SBATCH --job-name=mpi_test
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --output=mpi_job.out

# module load mpi  # Optional, if MPI needs to be loaded as a module
OMPI_ALLOW_RUN_AS_ROOT=1 OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1 srun ./hello_mpi

