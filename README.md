# Neh_flowshop
Implementation of the Neh algorithm in Python

[The Neh heuristic by Nawaz et al., 1983](https://www.sciencedirect.com/science/article/abs/pii/0305048383900889) is dubbed as an effective greedy heuristic algorithm for flow shop problems. 

Naturally, for a flowshop problem, the search space is bounded up to \( n! \) jobs. The heuristic reduces this space by

\
$\ \frac{\text{Number of permutations with Neh heuristic}}{n!} $ 



<details>
<summary>This algorithm has a time complexity O(nlogn)+O(n⋅m) , it runs the following steps:</summary>
<br>
# Pseudo Code for the Neh Algorithm

## Input:
- n: number of jobs
- m: number of machines
- processing_times: array of processing times for each job on each machine

## Output:
- schedule: a schedule that minimizes the makespan

## Procedure:
1. Compute the sum of each job across each machine, sort them in a decreasing order.
2. Initialize an empty schedule.
3. Using  the sorted order, as long as the schedule does not contain all the jobs:
   a. add the first job to the list
   b. create all the possible permutations by shifting the newly added job to the right up to n times .
   c. compute the makespan of the flowshop schedule and choose the permutation with the lowest makespan.
   d. increment n by 1 and choose the next job from the aformentioned order
   
5. Obtain the schedule.

## Pseudo Code:
```
1. Compute_sum_of_each_job_across_machines_and_sort()

2. Initialize an empty schedule.

3. Set n_jobs_added = 0

4. while len(n_jobs) != n :
   a. Add_job_to_schedule_at_index(n_jobs_added)
   b. Compute_makespan_for_all_possible_permutations()
   c. Choose_permutation_with_lowest_makespan()
   d. Increment n_jobs_added by 1

5. Return schedule
```
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

### Misc and final words:

Building the logic for computing the markspan across all the newly generated makespans was a challenge, everything else was a breeze, originally I was going to relay on using the itertools to generate permutations but that was unecessary. Optimization-wise, maybe someone out there made a better code, the algorithm is older than me. took aprox 4 hours to build and I am already happy with all of this. Consider [giving this song a shot](https://www.youtube.com/watch?v=lBdQEqgpGfM), I did discover it by lurking /mu while on a bus.


