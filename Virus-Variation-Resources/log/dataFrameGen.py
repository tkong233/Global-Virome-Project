from ecotypeUtils import *
from functools import reduce
from itertools import groupby
import pandas as pd

def flatten(l):
	return [item for sublist in l for item in sublist]

'''
take in iterable(key, value)
reduce by applying func to values with same key
'''
def reduceByKey(func, iterable):
    get_first = lambda p: p[0]
    get_second = lambda p: p[1]
    return map(
        lambda l: (l[0], reduce(func, map(get_second, l[1]))),
        groupby(sorted(iterable, key=get_first), get_first)
    )

'''
take in ecotype: ['host', 'host', 'host']
return [('host', 1), ('host', 1), ('host', 1)]
'''
def mapCounter(ecotype):
	return [(host, 1) for host in ecotype]


Ecotypes = readLog()
accession_host = readSource()
newLog = mapAccessionHost(Ecotypes, accession_host)
hosts = [(host, [0]*len(newLog)) for host in list(set(flatten(newLog)))]	# [('host', [0, 0, 0])]



for i, ecotype in enumerate(newLog):
	for host_in_ecotype in ecotype:
		for host in hosts:
			if host_in_ecotype == host[0]:
				host[1][i] += 1






