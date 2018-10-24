# def removeEOF(seq):
# 	s = ""
# 	snips = seq.split('\n')
# 	for i in seq:
# 		if(i != '\n'):
# 			s += i
# 	return s

def nameSeq(s):
	snips = s.split('\n')
	name = snips.pop(0)
	seq = ''
	for i in snips:
		seq += i[ :len(i) - 1]
	return [name, seq]

# nameSeq = [(name, seq)]
# gaps = set of gap colums that need to be removed
def findGaps(nameSeq):
	gaps = set()
	for a in nameSeq:
		for i in range(len(a[1])):
			if a[1][i] == '-':
				gaps.add(i)
	ls = list(gaps)
	ls.sort()
	return ls

def removeGaps(seq, gaps):
	acc = seq[:gaps[0]]
	for n in range(len(gaps) - 1):
		if(gaps[n+1] < len(seq)):
			l = gaps[n]
			r = gaps[n+1]
			acc += seq[l+1:r]
	acc += seq[gaps[len(gaps)-1]+1:]
	return acc


filename = input("please type the name of alignment sequence file to remove gaps: ")
file = open(filename, "r")
alignments = file.read().split('>')	# list of str
nameSeq = [nameSeq(s) for s in alignments if s != ''] #[(name, seq)]
print('>number of sequences: ', len(nameSeq))
print('>sequence length: ', len(nameSeq[0][1]), 'bp' )


gaps = findGaps(nameSeq)
print('>number of gaps found:', len(gaps))
nameSeq_ = [(name, removeGaps(seq, gaps)) for (name, seq) in nameSeq]
print('>sequence length after gaps removed: ', len(nameSeq_[0][1]), 'bp' )


#write resulting sequences to file, overwrite if existed
newFilename = ''
for s in filename.split('.'):
	if (s != 'fa') and (s != 'fasta'):
		newFilename += s
newFilename += '_removeGaps.fa'

file = open(newFilename, 'w+')
for seq in nameSeq_:
	file.write('>'+seq[0]+'\n')
	file.write(seq[1]+'\n')
file.close()