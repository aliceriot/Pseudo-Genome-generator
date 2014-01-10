import random

#get one random base pair (from actg)
def randactg(gc):
	x = random.random()
	if x > gc:
		y = random.choice('AT')
	else:
		y = random.choice('GC')
	return y

#get a random sequence length len
def createseq(length,gc):
	seq = ''
	for i in range(length):
		seq += randactg(gc)
	return seq

#write to a .fasta file with a given seqname, filename, and sequence
def wrfasta(seqname,filename,seq):
	writefile = open (filename, 'w')
	writefile.write('>' + seqname '\n')
	for i in seq:
		if i % 80 = 
	writefile.close()
	return None

#tie it all together: pass a seqname, filename, sequence length, and gc content and it will write you a file
def pseudonome(seqname,filename,length,gccont):
	seq = createseq(length,gccont)
	wrfasta(seqname,filename,seq)
	return None
	
	
