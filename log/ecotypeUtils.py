'''
read log in .txt format: Ecotype 1: [FJ159131, AY277251, FJ159129, FJ159130] ....
return [['Ecotype 1 accessions'], ['Ecotype 2 accessions']]
'''
def readLog():
	fileName = input('>ecotype simulation log file: ')
	file = open(fileName, 'r')
	Ecotypes = file.read().split('Ecotype')[1:]
	Ecotypes = [x.split('[')[1:] for x in Ecotypes]
	Ecotypes = [y[0].split(']')[0] for y in  Ecotypes]	#['Accessions']
	Ecotypes = [z.split(', ') for z in Ecotypes]	#[['Accession']]
	return Ecotypes

'''
read source code <tbody id= ...>
return [(accession, host)]
'''
def readSource():
	fileName = input(">web souce code file: ")
	file = open(fileName, 'r')
	entries = file.read().split("id=\"")
	hosts = [x for x in entries if x[:6] == 'vhost_']
	accession_host_raw = [y.split('\">') for y in hosts]
	accession_host = [(z[0].split('vhost_')[1], z[1].split('<')[0]) for z in accession_host_raw]
	return accession_host

'''
take in
Ecotypes: [['Ecotype 1 accessions'], ['Ecotype 2 accessions']]
accession_host: [(accession1, host1), (accession2, host2)]

return
newLog = [['host 1', 'host 2'], ['host 1']]
'''
def mapAccessionHost(Ecotypes, accession_host):
	newEcotype = []
	newLog = []
	for ecotype in Ecotypes:
		for accession in ecotype:
			newEcotype += [ahpair[1] for ahpair in accession_host if accession == ahpair[0]]
		newLog.append(newEcotype)
		newEcotype = []
	newLog = [x for x in newLog if x != []]
	return newLog

'''
take in newLog: [['Ecotype 1 host 1', 'Ecotype 1 host 2'], ['Ecotype 2 host 1']]
write to newfile: Ecotype 1: [host1, host2 ...]
'''
def writeLog(newLog):
	newFileName = input('>name output file: ')
	newFile = open(newFileName, 'w+')
	for i, s in enumerate(newLog):
		newFile.write('Ecotype ' + str(i + 1) + ': ' + str(s) + '\n')
	newFile.close()
