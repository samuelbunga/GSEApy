import re
import os
import gseapy
import argparse
import pandas as pd
from gsea.make_rnk import *
from indra.databases.uniprot_client import um
from gsea.argument_parser import parse_arguments
from indra.databases.hgnc_client import get_hgnc_from_mouse, get_hgnc_name





def mgi_to_hgnc_name(gene_list):
    """Convert given mouse gene symbols to HGNC equivalent symbols"""
    mouse_gene_name_to_mgi = {v: um.uniprot_mgi.get(k)
                              for k, v in um.uniprot_gene_name.items()
                              if k in um.uniprot_mgi}

    filtered_mgi = {mouse_gene_name_to_mgi[gene] for gene in gene_list
                    if gene in mouse_gene_name_to_mgi}
    if len(filtered_mgi) == 0:
        raise Exception('No genes found')
        
    hgnc_gene_set = dict()
    for mgi_id in filtered_mgi:
        hgnc_id = get_hgnc_from_mouse(mgi_id)
        hgnc_name = get_hgnc_name(hgnc_id)
    return hgnc_name




if __name__ == '__main__':
    args = parse_arguments()

    INDIR = args.input
    OUTDIR = args.output
    FORMAT = args.file_type
    DB = args.database

    if FORMAT == 'd':
        format_deseq2(INDIR, OUTDIR, DB)

    elif FORMAT == 's':
        format_seurat(INDIR, OUTDIR, DB)
