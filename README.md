# About
GSEApy is a tool to perform Gene Set Enrichment Analysis on differentially expressed genes outputs from DeSEQ2 or Seurat. \
This is wrapper around gseapy python package
```bash
https://gseapy.readthedocs.io/en/latest/
```

# How to use?
Clone this repository
```bash
git clone https://github.com/samuelbunga/GSEApy.git
```

Create a conda environment
```bash
conda create -n GSEApy python=3.8
conda activate GSEApy
pip install -r requirements.txt
```

Required pipeline arguments
```bash
optional arguments:
  -i INPUT, --input (Path to input folder)
  -o OUTPUT, --output (Path to output folder)
  -db DATABASE, --database (Path to database)
  -f FILE_TYPE, --format (Type of input files [s = Seurat or d = DESeq2])
```
Run pipeline
```bash
 python3 run_GSEA.py -i ./test_files/deseq2/Human/ \
 -o ./output/ \
 -db ./Database/c2.cp.kegg.v7.2.symbols.gmt \
 -f d
```
