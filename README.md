Add this repository as a submodule of new workflows via 'git submodule add https://github.com/mgildea87/cat_rename_init.git'

#Description of files
## cat_rename.py
This script:

		1. Concatenates fastq files for samples that were split over multiple sequencing lanes
		2. Renames the fastq files from the generally verbose ids given by the sequencing center to those supplied in the Samples_info.tab file.
		3. The sample name, condition, and replicate columns are concatenated and form the new sample_id_Rx.fastq.gz files
		4. This script is executed snakemake_init.sh prior to snakemake execution

## snakemake_init.sh
This bash script:

		1. loads the miniconda3/4.6.14 module
		2. Loads the conda environment (/gpfs/data/fisherlab/conda_envs/...). You can clone the conda environment using the CUT-RUN.yml file and modify this bash script to load the env.
		3. Executes snakemake