# Import modules

from radical.entk import Kernel
import sys
import time
from graph_tool.all import Graph

def vary_tasks(f):

    num_pipelines = 1
    num_stages = 1
    num_tasks = [1,10,100,1000,10000,100000]

    for tasks in num_tasks:
        print 'starting'
    
        start = time.time()
    
        # Create empty set of pipes which is equivalent to the entire application
        set_of_pipes=set()
        for pipe in range(num_pipelines):
    
            # Create empty graph for each pipe
            Gpipe=Graph()
        
            for stage in range(num_stages):
            
                # Create a set of tasks to be added to each stage
                set_of_tasks=frozenset([Kernel() for _ in range(tasks)])
        
                cur_stage = set_of_tasks
            
                # Add current stage to current pipe
                Gpipe.add_vertex(cur_stage)
        
            # Add current pipe to set of pipes
            set_of_pipes.add(Gpipe)
        
        end = time.time()
    
        f.write('pipes: %s, stages: %s, tasks: %s, time: %s\n'%(num_pipelines, num_stages, tasks, end-start))
        print 'pipes: %s, stages: %s, tasks: %s, time: %s\n'%(num_pipelines, num_stages, tasks, end-start)


def vary_stages(f):

    num_pipelines = 1
    num_stages = [1,10,100,1000,10000]
    num_tasks = 100

    for stages in num_stages:
        print 'starting'
        start = time.time()
    
        # Create empty set of pipes which is equivalent to the entire application
        set_of_pipes=set()
        for pipe in range(num_pipelines):
    
            # Create empty graph for each pipe
            Gpipe=nx.Graph()
        
            for stage in range(stages):
            
                # Create a set of tasks to be added to each stage
                set_of_tasks=set([Kernel() for _ in range(num_tasks)])
        
                cur_stage = set_of_tasks
            
                # Add current stage to current pipe
                Gpipe.add_nodes_from(cur_stage)
        
            # Add current pipe to set of pipes
            set_of_pipes.add(Gpipe)
        
        end = time.time()
    
        f.write('pipes: %s, stages: %s, tasks: %s, time: %s\n'%(num_pipelines, stages, num_tasks, end-start))
        print 'pipes: %s, stages: %s, tasks: %s, time: %s\n'%(num_pipelines, stages, num_tasks, end-start)


def vary_pipes(f):

    num_pipelines = [1,10,100,1000,10000]
    num_stages = 10
    num_tasks = 10

    for pipes in num_pipelines:
    
        start = time.time()
    
        # Create empty set of pipes which is equivalent to the entire application
        set_of_pipes=set()
        for pipe in range(pipes):
    
            # Create empty graph for each pipe
            Gpipe=nx.Graph()
        
            for stage in range(num_stages):
            
                # Create a set of tasks to be added to each stage
                set_of_tasks=set([Kernel() for _ in range(num_tasks)])
        
                cur_stage = set_of_tasks
            
                # Add current stage to current pipe
                Gpipe.add_nodes_from(cur_stage)
        
            # Add current pipe to set of pipes
            set_of_pipes.add(Gpipe)
        
        end = time.time()
    
        f.write('pipes: %s, stages: %s, tasks: %s, time: %s\n'%(pipes, num_stages, num_tasks, end-start))
        print 'pipes: %s, stages: %s, tasks: %s, time: %s\n'%(pipes, num_stages, num_tasks, end-start)

if __name__ == '__main__':

    f = open('gt_perfs.txt','w')

    vary_tasks(f)
    #vary_stages(f)
    #vary_pipes(f)

    f.close()
