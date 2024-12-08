#!/bin/bash
#SBATCH --job-name=mpi_test
#SBATCH --ntasks=1
#SBATCH --nodes=1
#SBATCH --output=mpi_job.out
export OMPI_ALLOW_RUN_AS_ROOT=1
export OMPI_ALLOW_RUN_AS_ROOT_CONFIRM=1
srun --mpi=pmix /shared/hello_mpi
exit 0