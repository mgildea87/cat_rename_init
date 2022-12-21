#!/bin/bash -l

while getopts ":c:w:" arg; do
    case $arg in
        c) conda_env=$OPTARG;;
        w) workflow=$OPTARG;;
    esac
done

module load miniconda3/cpu/4.9.2
conda activate /gpfs/data/fisherlab/conda_envs/"$conda_env"
mkdir fastq
if ! python cat_rename_init/cat_rename.py /fastq_directory/ "$workflow" ${1}; then
    echo "Exiting..."
    exit
fi

snakemake --cluster "sbatch -J {cluster.Job_name} --mem {cluster.Mem} -c {cluster.Cores} -p {cluster.Partition} -t {cluster.Time} --output {cluster.Error}" --cluster-config cluster_config.yml --jobs 6
snakemake --report snake_make_report.html
multiqc .