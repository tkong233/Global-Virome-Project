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
take in a log: a list of ecotypes, where each ecotype is a list of hosts
return a list of hosts paired with list of ints that count the host's occurrence in each ecotype
'''
def count(log):
	hosts = host_init(log)
	for i, ecotype in enumerate(log):
		for host_in_ecotype in ecotype:
			for host in hosts:
				if host_in_ecotype == host[0]:
					host[1][i] += 1
	return [[i[0]]+i[1] for i in hosts]

'''
take in
Ecotypes: [['Ecotype 1 accessions'], ['Ecotype 2 accessions']]
accession_host: [(accession1, host1, country1), (accession2, host2, country2)]

return
newLog = [ecotype1: [['host1', 'country1'], [host2', 'country2']]]
'''
def mapAccessionHost_(Ecotypes, accession_host_country):
	newEcotype = []
	newLog = []
	for ecotype in Ecotypes:
		for accession in ecotype:
			newEcotype += [ahpair[1] for ahpair in accession_host_country if accession == ahpair[0]]
		if(newEcotype != []):
			newLog.append(newEcotype)
		newEcotype = []
	# newLog = [x for x in newLog if x != []]
	return newLog

'''
takes in a log: a list of ecotypes, where each ecotype is a list of hosts
returns a dataframe where each row is a host, each col is an ecotype, and each entry is the count of host occurs in this ecotype
'''
def generateDF(log):
	countHost = count(log)
	col = ['Host']
	for i in range(len(log)):
		col += ['Ecotype ' + str(i+1)]
	df = pd.DataFrame(countHost, columns = col)
	return df

'''
takes in a list of entries
return a new list consists of entries with >= 5 items
'''
def aboveFive(log):
	return list(filter(lambda x: len(x)>=5, log))


Ecotypes = readLog()
accession_host = readxlsx()
log = aboveFive(mapAccessionHost_(Ecotypes, accession_host))
df = generateDF(log)
filename = input('>name output csv file: ')
df.to_csv(filename)





