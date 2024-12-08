#!/bin/bash
#SBATCH --job-name=test_job
#SBATCH --output=test_job.out
#SBATCH --nodes=1
#SBATCH --ntasks=1

echo "This is a test job"
