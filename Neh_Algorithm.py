import numpy as np


machines_jobs = np.array([[2, 3, 4, 5, 6, 7],[3, 4, 5, 6, 7, 8],[4, 5, 6, 7, 8, 9],[5, 6, 7, 8, 9, 10],[6, 7, 8, 9, 10, 11]])

if machines_jobs is None:
    print("FEED ME THE JOBS!")
    
    

    

def sums(machines_jobs):
    return np.argsort(np.sum(machines_jobs, axis=0))

jobs = sums(machines_jobs)


def permu(job_list):
    perms = []
    new_list = []
    for i in job_list:
        if len(new_list) == 0:
            new_list.append(i)
            perms.append(new_list)
        else:
            for j in range(len(new_list)+1):
                new_list.insert(j, i)
                perms.append(new_list)

    return perms


def makespan(jobs, machines):
   
    finish_times = np.zeros(machines.shape[0])

    
    for job in jobs:
        
        for i in range(machines.shape[0]):
           
            start_time = max(finish_times[i], finish_times[i-1] if i > 0 else 0)
          
            finish_times[i] = start_time + machines[i, job]

   
    return np.max(finish_times)


schedule = np.array([3,4,5])


def find_best_job_sequence(machines_jobs):

    jobs = sums(machines_jobs)
    

    job_seq = [jobs[0], jobs[1]]


    for i in range(2, len(jobs)):
        job = jobs[i]
        best_pos = None
        best_makespan = np.inf
        for j in range(len(job_seq) + 1):
            new_seq = job_seq[:j] + [job] + job_seq[j:]
            new_makespan = makespan(new_seq, machines_jobs)
            
            if new_makespan < best_makespan:
                best_makespan = new_makespan
                best_pos = j
                
        job_seq.insert(best_pos, job)
    return job_seq

print("Best job sequence: ", find_best_job_sequence(machines_jobs) , "with makespan: ", makespan(find_best_job_sequence(machines_jobs), machines_jobs))