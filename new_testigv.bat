new
genome /Users/petadimensionlab/ws/ref/genome/saimiri_ensembl
snapshotDirectory /Users/petadimensionlab/Downloads/test_igv/output/igv_dir
load /Users/petadimensionlab/Downloads/test_igv/output/igv_dir/SRR000000.Aligned.out.sorted.bam
load /Users/petadimensionlab/Downloads/test_igv/output/igv_dir/SRR000001.Aligned.out.sorted.bam
goto chr1:10000-20000
sort
collapse
snapshot chr1_10000-20000.svg
goto chr2:20000-30000
sort
collapse
snapshot chr2_20000-30000.svg
goto chr3:50000-70000
sort
collapse
snapshot chr3_50000-70000.svg