import os
import re
import sys

species = 'hg38'
genome_dir = '/Users/yourname/ws/ref/genome/' #your local genome dir
genomeFastaFile = os.path.join(genome_dir,species)

root_dir = '/Users/petadimensionlab/tmp/tmp/' #"root_dir" is "/yourlocal_dir" set by run.
igv_dir = os.path.join(root_dir,'igv_dir')


bed_file = 'cluster_Saimiri_boliviensis'


with open('/condir/igv_dir/igv.bat', 'w') as f:
    f.write(os.path.join("new\ngenome "+genomeFastaFile+"\n"+"snapshotDirectory "+igv_dir+"\n"))


sample_f = open('/condir/SRR_Acc_List.txt')
for line in sample_f:
        sample = line.strip()
        bam_f = "load %s/{}.Aligned.out.sorted.bam\n" %(igv_dir)
        bam_f = bam_f.format(sample)
        with open('/condir/igv_dir/igv.bat','a') as f:
                for bam in bam_f :
                        f.write(os.path.join(bam))

bed_f = open(os.path.join('/condir/',bed_file+'.bed'))
for line in bed_f:
        chrom,start,end,Class,_,strand,_ = line.strip().split()
        text = "goto {}:{}-{}\nsort\ncollapse\nsnapshot {}_{}-{}.svg"
        text = text.format(chrom, start, end, chrom, start, end)
        with open('/condir/igv_dir/igv.bat','a') as f:
                for goto in text, :
                        f.write(os.path.join(goto+'\n'))