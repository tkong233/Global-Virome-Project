from ecotypeUtils import *
from functools import reduce
from itertools import groupby
import pandas as pd

def flatten(l):
	return [item for sublist in l for item in sublist]

def hosts(log):
	return list(set(flatten(log)))

'''
take in a log: a list of ecotypes, where each ecotype is a list of hosts
return a list of distinct hosts paired with list of zeros correspond to number of ecotypes
'''
def host_init(hosts, log):
	return [[host, [0]*len(log)] for host in hosts]

'''
take in a log,
return a list of hosts paired with list of ints that count the host's occurrence in each ecotype
'''
def countHost(hosts, log):
	h = host_init(hosts, log)
	for i, ecotype in enumerate(log):
		for host_in_ecotype in ecotype:
			for host in h:
				if host_in_ecotype == host[0]:
					host[1][i] += 1
	return h

'''
takes in a log and returns a subset in which each ecotype has more than 5 samples
'''
def moreThanFive(log):
	return list(filter(lambda x: len(x)>=5, log))


log_all = moreThanFive(mapAccessionHost(readLog(), readSource()))
log_mosquito = mapAccessionHost(readLog(), readSource())
hosts_all = hosts(log_all)
hosts_mosquito = hosts(log_mosquito)
hosts_remove_mosquito = list(filter(lambda x: not x in hosts_mosquito, hosts_all))

print("number of all hosts: ", len(hosts_all))
print("number of mosquito hosts: ", len(hosts_mosquito))
print("number of hosts removed mosquito: ", len(hosts_remove_mosquito))

countHost = [[i[0]]+i[1] for i in countHost(hosts_remove_mosquito, log_all)]

col = ['Host']
for i in range(len(log_all)):
	col += ['Ecotype ' + str(i+1)]

df = pd.DataFrame(countHost, columns = col)
filename = input('>name output csv file: ')
df.to_csv(filename)





