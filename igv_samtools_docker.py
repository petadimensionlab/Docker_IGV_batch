## http://kazumaxneo.hatenablog.com/entry/2017/07/05/132019
import os

thread_num = 3

root_dir = '/condir/'
igv_dir = os.path.join(root_dir,'igv_dir')

### sort and index using samtools
fr = open(os.path.join(root_dir,'SRR_Acc_List.txt'),'r').readlines()
for line in fr:
    line = line.replace('\n','')
    lst = line.split(',')
    filename = lst[0]
    samplename = filename
    if not os.path.exists(igv_dir):
        os.mkdir(igv_dir)

    ### sort bam
    msg = '%s is now sorting...' % (samplename)
    print( msg )
    bamFile = os.path.join(root_dir,samplename+'.Aligned.out.bam')
    bamSortFile = os.path.join(igv_dir,samplename+'.Aligned.out.sorted.bam')

    cmd = 'samtools sort -@ %d -o %s %s' % (thread_num,bamSortFile,bamFile)
    print( cmd )
    os.system(cmd)

    ### index
    msg = '%s is now indexing...' % (samplename)
    print( msg )

    cmd = 'samtools index %s' % (bamSortFile)
    print( cmd )
    os.system(cmd)

    ## finish ##
    msg = '%s : finish!' % (samplename)
    print( msg )