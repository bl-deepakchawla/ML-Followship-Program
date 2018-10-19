import multiprocessing


def no_of_cpus_using():
    return multiprocessing.cpu_count()


total_cpu = no_of_cpus_using()
print("Total of CPU's using by your machine is", total_cpu)