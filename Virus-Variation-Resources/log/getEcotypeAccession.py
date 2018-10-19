logFileName = input('>ecotype simulation log file: ')
logFile = open(logFileName, 'r')
Ecotypes = logFile.read().split('Ecotype')[1:]
Ecotypes = [x.split('[')[1:] for x in Ecotypes]
Ecotypes = [y[0].split(']')[0] for y in  Ecotypes]	#['Accessions']
Ecotypes = [z.split(',') for z in Ecotypes]	#[['Accession']]


sourceFileName = input(">web souce code file: ")
source = open(sourceFileName, 'r')
entries = source.read().split("id=\"")
hosts = [x for x in entries if x[:6] == 'vhost_']
accession_host_raw = [y.split('\">') for y in hosts]
accession_host = [(z[0].split('vhost_')[1], z[1].split('<')[0]) for z in accession_host_raw]

newEcotype = []
newLog = []
for ecotype in Ecotypes:
	for ahpair in accession_host:
		newEcotype += [ahpair[1] for accession in ecotype if accession == ahpair[0]]
	newLog.append(newEcotype)

# print(Ecotypes)
# print(accession_host)
# print(newLog)
print('>number of ecotypes: ', len(Ecotypes))
print('>number of (accession, host)', len(accession_host))
print('>number of ecotypes in newLog: ', len(newLog))



newFileName = input('>name output file: ')
newFile = open(newFileName, 'w+')

for i, s in enumerate(newLog):
	newFile.write('Ecotype ' + str(i + 1) + ': ' + str(s) + '\n')

newFile.close()
