import os, subprocess, sys
import pandas as pd

#Combine fastq files from multiple lanes
#Run script inside fastq directory
def concat():
	cur_dir = 'fastq/'
	fast_dir = sys.argv[1]
	files = os.listdir(fast_dir)
	samples = {}
	for file in files:
		file = '%s%s' % (fast_dir, file)
		if 'L00' in file:
			if os.path.isfile(file) and file.endswith('fastq.gz'):
					a = file.split('L00')
					f = '%s%s' % (a[0], a[1][2:])
					if f not in samples:
						samples[f] = [file]
					else:
						samples[f].append(file)
		elif os.path.isfile(file) and file.endswith('fastq.gz'):
			samples[file] = [file]
	for sample in samples:
		com = samples[sample]
		com.sort()
		com.insert(0, 'cat')
		with open('%s%s' % (cur_dir, sample.split('/')[-1]), 'w') as R1:			
			subprocess.run(com, stdout=R1)

#rename samples based on sample ids in samples_info.tab. This differs with different workflows
def rename_RNA_SE():
	sample_file = "samples_info.tab"
	table = pd.read_table(sample_file)
	sample = table['Sample']
	replicate = table['Replicate']
	condition = table['Condition']
	File_R1 = table['File_Name_R1']

	for i in range(len(File_R1)):
		file = File_R1[i].split('L00')
		file = '%s%s' % (file[0], file[1][2:])
		if os.path.exists('fastq/%s_%s_%s_R1.fastq.gz' % (sample[i],condition[i],replicate[i])):
			continue
		if os.path.exists('fastq/%s' % (file)):
			os.system('mv fastq/%s fastq/%s_%s_%s_R1.fastq.gz' % (file,sample[i],condition[i],replicate[i]))
		elif os.path.exists('fastq/%s_%s_%s_R1.fastq.gz' % (sample[i],condition[i],replicate[i])) == False:
			print('fastq/%s or fastq/%s_%s_%s_R1.fastq.gz do not exist!' % (file, sample[i],condition[i],replicate[i]))
			sys.exit(1)

def rename_RNA_PE():
	sample_file = "samples_info.tab"
	table = pd.read_table(sample_file)
	sample = table['Sample']
	replicate = table['Replicate']
	condition = table['Condition']
	File_R1 = table['File_Name_R1']
	File_R2 = table['File_Name_R2']

	for i in range(len(File_R1)):
		file = File_R1[i].split('L00')
		file = '%s%s' % (file[0], file[1][2:])
		if os.path.exists('fastq/%s_%s_%s_R1.fastq.gz' % (sample[i],condition[i],replicate[i])):
			continue
		if os.path.exists('fastq/%s' % (file)):
			os.system('mv fastq/%s fastq/%s_%s_%s_R1.fastq.gz' % (file,sample[i],condition[i],replicate[i]))
		elif os.path.exists('fastq/%s_%s_%s_R1.fastq.gz' % (sample[i],condition[i],replicate[i])) == False:
			print('fastq/%s or fastq/%s_%s_%s_R1.fastq.gz do not exist!' % (file, sample[i],condition[i],replicate[i]))
			sys.exit(1)

	for i in range(len(File_R2)):
		file = File_R2[i].split('L00')
		file = '%s%s' % (file[0], file[1][2:])
		if os.path.exists('fastq/%s_%s_%s_R1.fastq.gz' % (sample[i],condition[i],replicate[i])):
			continue
		if os.path.exists('fastq/%s' % (file)):
			os.system('mv fastq/%s fastq/%s_%s_%s_R2.fastq.gz' % (file,sample[i],condition[i],replicate[i]))
		elif os.path.exists('fastq/%s_%s_%s_R2.fastq.gz' % (sample[i],condition[i],replicate[i])) == False:
			print('fastq/%s or fastq/%s_%s_%s_R2.fastq.gz do not exist!' % (file, sample[i],condition[i],replicate[i]))

def rename_ChIP():
	sample_file = "samples_info.tab"
	table = pd.read_table(sample_file)
	sample = table['Sample']
	replicate = table['Replicate']
	condition = table['Condition']
	Antibody = table['Antibody']
	File_R1 = table['File_Name_R1']
	File_R2 = table['File_Name_R2']

	for i in range(len(File_R1)):
		file = File_R1[i].split('L00')
		file = '%s%s' % (file[0], file[1][2:])
		if os.path.exists('fastq/%s_%s_%s_%s_R1.fastq.gz' % (sample[i],condition[i],replicate[i], Antibody[i])):
			continue
		if os.path.exists('fastq/%s' % (file)):
			os.system('mv fastq/%s fastq/%s_%s_%s_%s_R1.fastq.gz' % (file,sample[i],condition[i],replicate[i], Antibody[i]))
		elif os.path.exists('fastq/%s_%s_%s_%s_R1.fastq.gz' % (sample[i],condition[i],replicate[i], Antibody[i])) == False:
			print('fastq/%s or fastq/%s_%s_%s_%s_R1.fastq.gz do not exist!' % (file, sample[i],condition[i],replicate[i], Antibody[i]))
			sys.exit(1)

	for i in range(len(File_R2)):
		file = File_R2[i].split('L00')
		file = '%s%s' % (file[0], file[1][2:])
		if os.path.exists('fastq/%s_%s_%s_%s_R1.fastq.gz' % (sample[i],condition[i],replicate[i], Antibody[i])):
			continue
		if os.path.exists('fastq/%s' % (file)):
			os.system('mv fastq/%s fastq/%s_%s_%s_%s_R2.fastq.gz' % (file,sample[i],condition[i],replicate[i], Antibody[i]))
		elif os.path.exists('fastq/%s_%s_%s_%s_R2.fastq.gz' % (sample[i],condition[i],replicate[i], Antibody[i])) == False:
			print('fastq/%s or fastq/%s_%s_%s_%s_R2.fastq.gz do not exist!' % (file, sample[i],condition[i],replicate[i], Antibody[i]))
			sys.exit(1)

concat()

if sys.argv[2] == 'CUT-RUN' or sys.argv[2] == 'ChIPseq':
	rename_ChIP()
if sys.argv[2] == 'RNAseq_PE' or sys.argv[2] == 'RNAseq_PE_HISAT2_stringtie' or sys.argv[2] == 'RNAseq_PE_HISAT2_stringtie_novel_transcripts':
	rename_RNA_PE()
if sys.argv[2] == 'RNAseq_SE':
	rename_RNA_SE()