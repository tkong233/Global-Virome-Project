from ecotypeUtils import *

Ecotypes = readLog()
accession_host = readSource()
newLog = mapAccessionHost(Ecotypes, accession_host)
newLog = list(filter(lambda x: len(x)>=5, newLog))


writeLog(newLog)

print('>number of ecotypes: ', len(Ecotypes))
print('>number of (accession, host)', len(accession_host))
print('>number of ecotypes in new log: ', len(newLog))


