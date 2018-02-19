# QuickTools

Andreas Novotny

Small tools for solving various bioinformatic problems.

---

## ReMinDeR
Written for python3

Quick conversion of R markdown files to basic R scripts.
Quick conversion of R scripts to basic R markdown scripts.

**Usage:**

`python3 ReMinDeR.py file_Rmd file_R input_format`

---

## CSVtoFASTA

Written for python3

Converts a CSV file containing a list of sequences (as obtained by the get.sequences() in dada2),
and converts it to a handy FASTA format, where the sequence is its own name:

`>ATGTCGTA`

`ATGTCGTA`

**Usage:**

`python3 CSVtoFASTA.py input_file.csv output_file.fa`
