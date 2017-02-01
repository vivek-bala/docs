# Import modules

from radical.entk import Kernel
import sys
import time

def vary_tasks(f):

    num_pipelines = 1
    num_stages = 1
    num_tasks = [1,10,100,1000,10000,100000]

    for tasks in num_tasks:
        start = time.time()
    
        set_of_tasks = frozenset([Kernel() for _ in range(tasks)]) # equivalent to one stage
        list_stages = tuple([set_of_tasks for _ in range(num_stages)]) # equivalent to one pipe
        set_of_pipelines = set([list_stages for _ in range(num_pipelines)]) # equivalent to one application
        end = time.time()
    
        f.write('pipes: %s, stages: %s, tasks: %s, time: %s\n'%(num_pipelines, num_stages, tasks, end-start))


def vary_stages(f):

    num_pipelines = 1
    num_stages = [1,10,100,1000,10000,100000]
    num_tasks = 100000

    for stages in num_stages:
    
        start = time.time()
        set_of_tasks = frozenset([Kernel() for _ in range(num_tasks)]) # equivalent to one stage
        list_stages = tuple([set_of_tasks for _ in range(stages)]) # equivalent to one pipe
        set_of_pipelines = set([list_stages for _ in range(num_pipelines)]) # equivalent to one application
        end = time.time()
    
        f.write('pipes: %s, stages: %s, tasks: %s, time: %s\n'%(num_pipelines, stages, num_tasks, end-start))

def vary_pipes(f):

    num_pipelines = [1,10,100,1000,10000,100000]
    num_stages = 100000
    num_tasks = 100000

    for pipes in num_pipelines:
    
        start = time.time()
        set_of_tasks = frozenset([Kernel() for _ in range(num_tasks)]) # equivalent to one stage
        list_stages = tuple([set_of_tasks for _ in range(num_stages)]) # equivalent to one pipe
        set_of_pipelines = set([list_stages for _ in range(pipes)]) # equivalent to one application
        end = time.time()
    
        f.write('pipes: %s, stages: %s, tasks: %s, time: %s\n'%(pipes, num_stages, num_tasks, end-start))


if __name__ == '__main__':

    f = open('list_perfs.txt','w')

    vary_tasks(f)
    vary_stages(f)
    vary_pipes(f)

    f.close()
