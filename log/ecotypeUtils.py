import xlrd
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

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
read an excel worksheet and return a list of entries where each entry consists of the items in a row,
e.g.: [[accession, host, country], [accession, host, country]]
'''
def readxlsx():
	sc = input('>name of accession xlsx file: ')
	loc = (dir_path + '/' + sc)
	wb = xlrd.open_workbook(loc) 
	sheet = wb.sheet_by_index(0) 
	col = sheet.ncols
	row = sheet.nrows
	all = []
	for x in range(row):
		entry = []
		for y in range(col):
			entry += [sheet.cell_value(x, y)]
		all.append(entry)
	return all

'''
take in
Ecotypes: [['Ecotype 1 accessions'], ['Ecotype 2 accessions']]
accession_host: [(accession1, host1, country1), (accession2, host2, country2)]

return
newLog = [ecotype1: [['accession1', 'host1', 'country1'], ['accession2', 'host2']]]
'''
def mapAccessionHost(Ecotypes, accession_host_country):
	newEcotype = []
	newLog = []
	for ecotype in Ecotypes:
		for accession in ecotype:
			newEcotype += [ahpair for ahpair in accession_host_country if accession == ahpair[0]]
		if(newEcotype != []):
			newLog.append(newEcotype)
		newEcotype = []
	# newLog = [x for x in newLog if x != []]
	return newLog


