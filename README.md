# Neh_flowshop
Implementation of the Neh algorithm in Python

[The Neh heuristic by Nawaz et al., 1983](https://www.sciencedirect.com/science/article/abs/pii/0305048383900889) is dubbed as an effective greedy heuristic algorithm for flow shop problems. 

Naturally, for a flowshop problem, the search space is bounded up to \( n! \) jobs. The heuristic reduces this space by

\
$\ \frac{\text{Number of permutations with Neh heuristic}}{n!} $ 



<details>
<summary>This algorithm has a time complexity O(nlogn)+O(n⋅m) , it runs the following steps:</summary>
<br>
Input:
- Job_dict: Dictionary containing job processing times for each machine
- num_machines: Number of machines

Output:
- best_schedule: The best job schedule found by the Neh heuristic
- best_makespan: The makespan associated with the best schedule

Algorithm:
1. For each job, compute its sum across all the machines.
2. Initialize an empty schedule with 'num_machines' machines.
3. For each job in the sorted order:
     a. Assign the job to the machine with the minimum total processing time.
4. Calculate the makespan for the final schedule.

Pseudo-code:
function Neh(Job_dict, num_machines):
    job_sums = {job: sum(Job_dict[job]) for job in Job_dict}
    sorted_jobs = sort jobs in non-increasing order of job_sums

    schedule = [[] for _ in range(num_machines)]
    for job in sorted_jobs:
        min_machine = machine with the minimum total processing time in schedule
        min_machine.append(job)

    final_schedule = [[job_index + 1 for job_index in machine] for machine in schedule]
    best_makespan = max(sum(Job_dict[final_schedule[-1][i]][i] for i in range(num_machines)),
                        sum(Job_dict[final_schedule[-1][i]][i] for i in range(num_machines - 1, -1, -1)))

    return final_schedule, best_makespan



</details>


In this repo you will find an easy to use Python script that implements the algorithm. 

## How to use:

1. Fill the machines_jobs variable with a multi-dimensional matrix array that contains the processing times, each  array represents a machine, each inner value represents the processing times of the $j$ jobs in the given machine. Dealing with dictionaries is slow and made it hard for me to build the logic of the code, arrays shall it be! check the example at the end
2. This is a flow shop problem, each job will be processed once on each machine, I did not add a function that checks if all the processing times are inside. Make sure everything is inside
3. Run it and let it do its magic, you will get a permutation together with its makespan.

Example: 
To repsent this matrix within the array:

| Machines / Jobs  | Job 1 | Job 2  | Job 3  | Job 4 | Job 5 | Job 6|
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Machine 1| 2  | 3  | 4  | 5  | 6  | 7  |
| Machine 2  | 3  | 4  | 5 | 6  | 7  |8  |
| Machine 3  | 4  | 5 | 6  | 7  | 8  | 9  |
| Machine 4  | 5  | 6  | 7  | 8  | 9  | 10  |
| Machine 5  | 6  | 7  | 8  | 9 | 10  | 11  |


You just fill the variable like so:
```[python]
machines_jobs = np.array([[2, 3, 4, 5, 6, 7],[3, 4, 5, 6, 7, 8],[4, 5, 6, 7, 8, 9],[5, 6, 7, 8, 9, 10],[6, 7, 8, 9, 10, 11]])
```




