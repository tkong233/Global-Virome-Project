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


# Ecotypes = readLog()
# accession_host = readSource()

log_all = mapAccessionHost(readLog(), readSource())
log_all = list(filter(lambda x: len(x)>=5, log_all))
log_mosquito = mapAccessionHost(readLog(), readSource())
# print('number of ecotypes in log_all: ', len(log_all))
hosts_all = hosts(log_all)
# print('host_all', hosts_all)
print("number of all hosts: ", len(hosts_all))
hosts_mosquito = hosts(log_mosquito)
print("number of mosquito hosts: ", len(hosts_mosquito))
hosts_remove_mosquito = list(filter(lambda x: not x in hosts_mosquito, hosts_all))
print("number of hosts removed mosquito: ", len(hosts_remove_mosquito))

# print("hosts removed mosquito:", hosts_remove_mosquito)
# print('init host: ', host_init(hosts_remove_mosquito, log_all))
print('len init host: ', len(host_init(hosts_remove_mosquito, log_all)))

# print(countHost(hosts_remove_mosquito, log_all))

# countHost = countHost(log_all, hosts_remove_mosquito)
# print('len countHost: ', len(countHost))
# print('len countHost[1]', len(countHost[1]))
# print(countHost)

countHost = [[i[0]]+i[1] for i in countHost(hosts_remove_mosquito, log_all)]
# print("should be number of rows(hosts except mos): ", len(countHost))
# print("should be number of cols(#ecotype + 1): ", len(countHost[0]))

col = ['Host']
for i in range(len(log_all)):
	col += ['Ecotype ' + str(i+1)]

df = pd.DataFrame(countHost, columns = col)

# print(df)
filename = input('>name output csv file: ')
df.to_csv(filename)





