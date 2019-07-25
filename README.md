# Docker_IGV_batch
これはIGV（batchスクリプト作成用）のdockerイメージです / This is a docker image for IGV.(For batch script creation) 
また、samtoolsも使用できます / Can also samtools this docker　image.

## 1.Usage
#### docker pull image

```
docker pull petadimensionlab/docker_igv_batch
```

#### docker run

```
docker run -it --name container_name -v /yourlocal_dir:/condir --rm petadimensionlab/docker_igv_batch
```
Copy your "bam file" , "bed file" and "sampleID list text" into the "/yourlocal_dir" .

example ""sampleID list text""data = https://github.com/petadimensionlab/Docker_IGV_batch/blob/master/SRR_Acc_List.txt

#### Run python into this docker
```
# python3 /tmp/igv_samtools_docker.py
```
* igv_samtools_docker.py = Samtools sorting and indexing

```
# python3 tmp/igv_batch_docker.py
```
* igv_batch_docker.py = Create an IGV batch scrip

All execution result is output to the "/yourlocal_dir".

### Running IGV with a batch file
can load a batch file by using " Tools > Run Batch Script ".

Manual page here:https = https://software.broadinstitute.org/software/igv/batch

#### exit docker
```
/ # exit
```
