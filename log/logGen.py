from ecotypeUtils import *

'''
take in newLog: [['Ecotype 1 host 1', 'Ecotype 1 host 2'], ['Ecotype 2 host 1']]
write to newfile: Ecotype 1: [host1, host2 ...]
'''
def writeLog(newLog):
	newFileName = input('>name output txt file: ')
	newFile = open(newFileName, 'w+')
	for i, s in enumerate(newLog):
		newFile.write('Ecotype ' + str(i + 1) + ': ' + str(s) + '\n')
	newFile.close()

Ecotypes = readLog()
accession = readxlsx()
newLog = mapAccessionHost(Ecotypes, accession)
# newLog = list(filter(lambda x: len(x)>=5, newLog))


writeLog(newLog)

print('>number of ecotypes in original log: ', len(Ecotypes))
print('>number of (accession, host)', len(accession))
print('>number of ecotypes in new log: ', len(newLog))


