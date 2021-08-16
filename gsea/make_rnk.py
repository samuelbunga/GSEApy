import os
import re
import logging
import pandas as pd


logger = logging.getLogger()

'''
def make_rnk_files(files, DB):
    for f in files:
        file = pd.read_csv(os.path.join(WD, 'DEG_CLUSTER/', f),
                           header=0, index_col=0)
        genes, p_adj = [], []
        for r, c in file.iterrows():
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
        rnk_file.to_csv(os.path.join(WD, 'rnk', f_name + '.rnk'),
                        index=False,
                        sep='\t',
                        header=False)
        # Run GSEA
        try:
            os.mkdir(os.path.join(WD, 'outputs', DB, f_name), exist_ok=True)
        except:
            pass
        gseapy.prerank(os.path.join(WD, 'rnk', f_name + '.rnk'),
                       os.path.join(WD, 'Database/c2.cp.kegg.v7.2.symbols.gmt'),
                       os.path.join(WD, 'outputs', DB, f_name)
'''

def make_rnk(genes, padj, f, outdir):
    logger.info("Creating rank file for {}".format(os.path.basename(f)))
    # create rank dir
    os.mkdir(os.path.join(outdir, 'rnk'), exist_ok=True)

    fname = os.path.basename(f)

    rnk_file = pd.DataFrame({'names': genes,
                             'p_adj': p_adj})

    rnk_file.to_csv(os.path.join(os.path.realpath(outdir),
                                 'rnk', fname + '.rnk'),
                    index=False,
                    sep='\t',
                    header=False)
    logger.info("Success!")
    l

def format_deseq2(indir, outdir):
    files = [f for f in os.listdir(os.path.realpath(indir)) if re.search(r'.*csv', f)]

    for f in files:
        logger.info("Processing {}".format(os.path.basename(f)))
        df = pd.read_csv(os.path.realpath(f), header=0, index_col=0)

        genes, p_adj = [], []
        for r, c in df.iterrows():
            p_adj.append(c[5])
            genes.append(r)

        make_rnk(genes, padj, f, outdir)





