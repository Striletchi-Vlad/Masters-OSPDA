#include <mpi.h>
#include <stdio.h>
#include <unistd.h> // For sleep()

#define TOTAL_TASKS 10 // Predefined total number of sleep tasks

int main(int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int world_size, world_rank;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    // Calculate number of tasks per process and the remainder
    int tasks_per_process = TOTAL_TASKS / world_size;
    int extra_tasks = TOTAL_TASKS % world_size;

    // Determine the number of tasks for this process
    int num_tasks = tasks_per_process + (world_rank < extra_tasks ? 1 : 0);

    printf("Process %d performing %d tasks\n", world_rank, num_tasks);

    // Perform the assigned sleep tasks
    for (int i = 0; i < num_tasks; i++) {
        printf("Process %d performing task %d\n", world_rank, i + 1);
        sleep(1); // Sleep for 1 second
    }

    MPI_Finalize();
    return 0;
}
