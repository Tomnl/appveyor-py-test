#!/usr/bin/python
# File: sum_primes.py
# Author: VItalii Vanovschi
# Desc: This program demonstrates parallel computations with pp module
# It calculates the sum of prime numbers below a given integer in parallel
# Parallel Python Software: http://www.parallelpython.com

import math, sys, time
import pp

from multiprocessing import freeze_support

def isprime(n):
    """Returns True if n is prime and False otherwise"""
    if not isinstance(n, int):
        raise TypeError("argument passed to is_prime is not of 'int' type")
    if n < 2:
        return False
    if n == 2:
        return True
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    while i <= max:
        if n % i == 0:
            return False
        i += 1
    return True

def mzml2isa_stuff(filepth):
    from mzml2isa import mzml

    p = mzml.mzMLmeta(filepth).meta_isa

    return p



if __name__ == '__main__':
    freeze_support()
    # tuple of all parallel python servers to connect with
    ppservers = ()
    # ppservers = ("10.0.0.1",)

    if len(sys.argv) > 1:
        ncpus = int(sys.argv[1])
        # Creates jobserver with ncpus workers
        job_server = pp.Server(ncpus, ppservers=ppservers)
    else:
        # Creates jobserver with automatically detected number of workers
        job_server = pp.Server(ppservers=ppservers)

    start_time = time.time()

    # The following submits 8 jobs and then retrieves the results
    inputs = ('C:/DATA/test/A01_Polar_Daph_WAX4_Phenyl_LCMS_Neg_DIMS.mzML',
              'C:/DATA/test/A01_Polar_Daph_WAX4_Phenyl_LCMS_Neg_DIMS.mzML')

    jobs = []



    for i in inputs:
        jobs.append(job_server.submit(mzml2isa_stuff, (i,)))

    for j in jobs:
        print j()

    # jobs = [(input, job_server.submit(mzml2isa_stuff((input,), (isprime,), ("mzml2isa",))) for input in inputs]
    #print jobs


