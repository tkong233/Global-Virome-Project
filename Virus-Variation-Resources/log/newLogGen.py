from ecotypeUtils import *

Ecotypes = readLog()
accession_host = readSource()
newLog = mapAccessionHost(Ecotypes, accession_host)
writeLog(newLog)

print('>number of ecotypes: ', len(Ecotypes))
print('>number of (accession, host)', len(accession_host))


