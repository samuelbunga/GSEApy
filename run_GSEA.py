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


def make_rnk_files(files, DB):
    
    for f in files: 
        file = pd.read_csv(os.path.join(WD, 'DEG_CLUSTER/', f), 
                           header=0, index_col=0)
        genes, p_adj = [], []
        for r,c in file.iterrows():
            try:
                hgnc_symbol = mgi_to_hgnc_name([r])
                if hgnc_symbol != None:
                    genes.append(hgnc_symbol)
                    p_adj.append(c[4])
            except:
                continue
            
        rnk_file = pd.DataFrame({'names': genes, 
                                 'p_adj': p_adj})
        f_name = str(re.search('[a-zA-Z0-9_]+', f).group())
        rnk_file.to_csv(os.path.join(WD, 'rnk', f_name+'.rnk'),
                       index=False,
                       sep='\t',
                       header=False)
        # Run GSEA
        try:
            os.mkdir(os.path.join(WD, 'outputs', DB, f_name), exist_ok=True)
        except:
            pass
        gseapy.prerank(os.path.join(WD, 'rnk', f_name+'.rnk'),
                       os.path.join(WD, 'Database/c2.cp.kegg.v7.2.symbols.gmt'),
                       os.path.join(WD, 'outputs', DB, f_name)
                      )

if __name__ == '__main__':
    args = parse_arguments()

    INPUT = args.input
    OUTPUT = args.output
    FORMAT = args.file_type

    if FORMAT == 'de':
        format_deseq2("/Users/sbunga/gitHub/GSEApy/test_files/deseq2")
    '''
    try:
        os.mkdir(os.path.join(WD, 'rnk'))
    except FileExistsError:
        pass

    _, _, files = next(os.walk(os.path.join(WD, 'DEG_CLUSTER')))


    make_rnk_files(files, 'KEGG')
    '''
