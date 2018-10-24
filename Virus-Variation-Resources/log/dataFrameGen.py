from ecotypeUtils import *
from functools import reduce
from itertools import groupby
import pandas as pd

def flatten(l):
	return [item for sublist in l for item in sublist]

'''
take in a log: a list of ecotypes, where each ecotype is a list of hosts
return a list of distinct hosts paired with list of zeros correspond to number of ecotypes
'''
def host_init(log):
	return [[host, [0]*len(log)] for host in list(set(flatten(log)))]

'''
take in a log,
return a list of hosts paired with list of ints that count the host's occurrence in each ecotype
'''
def countHost(log):
	hosts = host_init(log)
	for i, ecotype in enumerate(log):
		for host_in_ecotype in ecotype:
			for host in hosts:
				if host_in_ecotype == host[0]:
					host[1][i] += 1
	return hosts


Ecotypes = readLog()
accession_host = readSource()

log = mapAccessionHost(Ecotypes, accession_host)
log = list(filter(lambda x: len(x)>=5, log))
countHost = [[i[0]]+i[1] for i in countHost(log)]

col = ['Host']
for i in range(len(log)):
	col += ['Ecotype ' + str(i+1)]

df = pd.DataFrame(countHost, columns = col)

filename = input('>name output csv file: ')
df.to_csv(filename)





