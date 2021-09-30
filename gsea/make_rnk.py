import os
import re
import gseapy
import logging
import pandas as pd


logger = logging.getLogger()


def run_gsea(indir, outdir, fname, db):
    if not os.path.isdir(os.path.join(outdir, 'gsea_out')):
        os.mkdir(os.path.join(outdir, 'gsea_out'))
    gseapy.prerank(os.path.join(outdir, 'rnk', fname + '.rnk'),
                   os.path.realpath(db),
                   os.path.join(outdir, 'gsea_out', fname))


def make_rnk(genes, p_adj, f, indir, outdir, db):
    logger.info("Creating rank file for {}".format(os.path.basename(f)))
    # create rank dir
    if not os.path.isdir(os.path.join(outdir, 'rnk')):
        os.mkdir(os.path.join(outdir, 'rnk'))

    fname = os.path.basename(f)

    rnk_file = pd.DataFrame({'names': genes,
                             'p_adj': p_adj})

    rnk_file.to_csv(os.path.join(os.path.realpath(outdir),
                                 'rnk', fname + '.rnk'),
                    index=False,
                    sep='\t',
                    header=False)

    logger.info('Starting gsea')
    run_gsea(indir, outdir, fname, db)
    logger.info("Success!")


def format_deseq2(indir, outdir, db):
    files = [f for f in os.listdir(os.path.realpath(indir))
             if re.search(r'.*csv', f)]

    for f in files:
        f = os.path.join(indir, f)
        logger.info("Processing {}".format(os.path.basename(f)))
        df = pd.read_csv(os.path.realpath(f), header=0, index_col=0)

        genes, stat = [], []
        for r, c in df.iterrows():
            stat.append(c[4])
            genes.append(r)

        make_rnk(genes, stat, f, indir, outdir, db)


def format_seurat(indir, outdir, db):
    files = [f for f in os.listdir(os.path.realpath(indir))
             if re.search(r'.*csv', f)]

    for f in files:
        f = os.path.join(indir, f)
        logger.info("Processing {}".format(os.path.basename(f)))
        df = pd.read_csv(os.path.realpath(f), header=0, index_col=0)

        genes, p_adj = [], []
        for r, c in df.iterrows():
            p_adj.append(c[4])
            genes.append(r)

        make_rnk(genes, p_adj, f, indir, outdir, db)
