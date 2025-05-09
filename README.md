# Enterobacter-TAOG-Finder  
Easy to identify T6SS-associated ortholog groups in *Enterobacter* genomes.

## Usage
The locus_finder.py can detect T6SS loci from *Proteinortho v6.2.3* output csv files. You can run it through python3 when giving it a csv file and it will directly output results on the screen.

```shell
python3 locus_finder.py <myproject.proteinortho.tsv>
```
After collecting all the T6SS distribution in *Enterobacter*, you can canculate the P/A-Value of all the ortholog groups. First you use *CD-HIT v4.6* to cluster all the *Enterobacter* proteins, and then you can get the output as a txt file. Name this file `input.txt` as the cdhit2matrix_merge.py input you will get a output file named `output_matrix.txt`, a TXT file as well.

```shell
python3 cdhit2matrix_merge.py <input.txt>
```
Rename the `output_matrix.txt` as `orthologue_file.txt`, it can be the Comparative_T6SS.py input file. This script can canculate the *P/A-Value*, means the ratio of the number of proteins exist in genomes have complete T6SS and have no T6SS.

```shell
python3 Comparative_T6SS.py <orthologue_file.txt> <presence_genomes.txt> <absence_genomes.txt>
```
The `presence_genomes.txt` and the `absence_genomes.txt` are the files contain which genomes contain complete T6SS and no T6SS. When you found all the T6SS-associated ortholog groups, you can find all the proteins connected in genomics through `findconnected.py`. You just need to put the proteins in a file as input then the output will show on the screen.
```shell
python3 findconnected.py <positive_ID>
```

You can find all the example files in Datasets documents.

